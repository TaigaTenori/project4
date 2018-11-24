from flask import Flask, render_template, request, redirect, session
import os
from flask_pymongo import PyMongo

import time
from bson.objectid import ObjectId
import json
from flask_mongo_sessions import MongoDBSessionInterface
from werkzeug.security import generate_password_hash, \
     check_password_hash

import re


app = Flask(__name__)

app.config['MONGO_DBNAME'] = "cookbook"
app.config['MONGO_URI'] = "mongodb://admin:verysecret12@ds241012.mlab.com:41012/cookbook"


mongo = PyMongo(app)



with app.app_context():
    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')



@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('login')
    


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return render_template('login.html', msg = "Already logged in", user = session['user'])

    if request.method == 'POST':
        user = mongo.db.users.find_one({ "name": request.form['user'] })
        if user:
            if check_password_hash(user['password'], request.form['password']):
                session['user'] = user['name']
                return render_template('login.html', user = session['user'], msg = "Login successful")
        
    return render_template('login.html')
    
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        user = mongo.db.users.find_one({ "name": request.form['user'] })
        if user:
            return render_template('register.html', msg = "User with this name already exists", form = request.form) # send the form back so we can prefill the inputs for another attempt.
        else:
            mongo.db.users.insert_one( { "name" : request.form['user'], "email" : request.form['email'], "password" : generate_password_hash(request.form['password'])})
            return render_template('login.html', msg = 'Registration successful - you can now log in.' )
    
    return render_template('register.html')
        
@app.route('/')
@app.route('/deleted')
@app.route('/edited')
def index():
    return render_template('index.html', recipies = mongo.db.recipies.find())
    

@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        term = request.form['search_for']

        return render_template('search.html',
                                results = mongo.db.recipies.find(
                                    {'$or':[ { 'ingredients.{}'.format(term.lower()): {'$exists' : 'true' } },
                                             { 'title': re.compile(term, re.IGNORECASE)} ] }
                                             ))
    return render_template('search.html')
    
@app.route('/sort/<sort_by>/<ad>')
def index_sorted(sort_by, ad):
    if ad == 'asc':
        direction = 1
    else:
        direction = -1

    return render_template('index.html', sort = "{} ({})".format(sort_by, ad), recipies = mongo.db.recipies.find().sort([ (sort_by, direction) ]))
    
@app.route('/add_recipe')
def add_recipe():
    if not 'user' in session:
        return redirect('login')
    return render_template('add_recipe.html', categories = mongo.db.categories.find())

@app.route('/insert_recipe', methods= ['POST'])
def insert_recipe():
    if not 'user' in session or session['user'] != request.form['username']:
        return redirect('login')
    
    tmp_dict = {}
    tmp = request.form.to_dict()

    for k, ingredient_name in tmp.items():
        s = k.split('ingredient')
        if len(s) > 1:
            tmp_dict[ingredient_name.lower()] = tmp['quantity' + s[1]]

    tmp['ingredients'] = tmp_dict
    
    # Much easier to store it here than use mongodb's aggregate() later
    tmp['ingredients_count'] = len(tmp_dict)
    
    # remove keys we won't be using
    for k in tmp.keys():
      if k != 'ingredients' and (k.startswith('ingredient') or k.startswith('quantity')):
        tmp.pop(k)
        
    del tmp['action']
    
    # last we need to add keys for date and upvotes
    
    tmp['date_added'] = time.ctime();
    tmp['upvotes'] = 0
    
    mongo.db.recipies.insert_one(tmp)
    return redirect('/')
    
    # 
    # return render_template('index.html', dic = tmp)
    
    
    
@app.route('/details/<recipe_id>')
def recipe_details(recipe_id):
    
    return render_template('recipe_details.html', recipe = mongo.db.recipies.find_one({ '_id': ObjectId(recipe_id) }))

@app.route('/edit/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipies.find_one({'_id': ObjectId(recipe_id) })
    if 'user' in session and recipe['username'] == session['user']:
        ingredients = recipe['ingredients']
        return render_template('edit_recipe.html',categories = mongo.db.categories.find(), recipe = recipe, ingredients = ingredients )

@app.route('/delete/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipies.find_one({'_id': ObjectId(recipe_id) })
    if 'user' in session and recipe['username'] == session['user']:
        mongo.db.recipies.delete_one({'_id': ObjectId(recipe_id) })
        return redirect('/deleted')
    
@app.route('/action/<recipe_id>', methods=["POST"])
def decide_action(recipe_id):
    recipe = mongo.db.recipies.find_one({'_id': ObjectId(recipe_id) })
    if 'user' in session and recipe['username'] == session['user']:
        if 'edit_button' in request.form.to_dict():
            return edit_recipe(recipe_id)
        else:
            return delete_recipe(recipe_id)

    return redirect('/')
    
@app.route('/update/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    # apparently not really an update, but same experience for the user and less code and more elegant I think.
   insert_recipe()
   mongo.db.recipies.delete_one({'_id': ObjectId(recipe_id) })
   return redirect('/')


# This is AJAX only
@app.route('/upvote/<recipe_id>', methods=["POST"])
def upvote_recipe(recipe_id):

    mongo.db.recipies.update({ '_id': ObjectId(recipe_id) }, { '$inc': { 'upvotes': 1 }})
    return "OK"


@app.route("/summary")
def summary():

    # find categories and count how many documents each of them has
    
    d = mongo.db.recipies.aggregate([
            { '$group': { '_id': '$category', 'count': {'$sum':1} } },
            { '$sort': { 'count': -1} } # Can't use .sort with aggregate

        ])
 
    return render_template('summary.html', result = d)

if __name__ == '__main__':
    app.run(host = os.getenv('IP', '0.0.0.0'),
            port = os.getenv('PORT', '8080'),
            debug = True
            )