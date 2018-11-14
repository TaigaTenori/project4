from flask import Flask, render_template, request, redirect
import os
from flask_pymongo import PyMongo
import time
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "cookbook"
app.config['MONGO_URI'] = "mongodb://admin:verysecret12@ds241012.mlab.com:41012/cookbook"

mongo = PyMongo(app)
@app.route('/')
def index():
    return render_template('index.html', recipies = mongo.db.recipies.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', categories = mongo.db.categories.find())

@app.route('/insert_recipe', methods= ['POST'])
def insert_recipe():
    
    
    
    tmp = request.form.to_dict()
    tmp['ingredients'] =  tmp['ingredients'].replace('\r\n', ',')
    tmp['quantities'] = tmp['quantities'].replace('\r\n', ',') 
    
    # string.split() creates a list
    l_one = tmp['ingredients'].split(',')
    l_two = tmp['quantities'].split(',')
    
    # We need to combine ingredients and quantities into a nested dictionary
    tmp_dict = dict(zip(l_one, l_two))
    tmp['ingredients'] = tmp_dict
    
    
    # remove keys we won't be using
    del tmp['ingredient']
    del tmp['quantity']
    del tmp['quantities']
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

if __name__ == '__main__':
    app.run(host = os.getenv('IP', '0.0.0.0'),
            port = os.getenv('PORT', '8080'),
            debug = True
            )