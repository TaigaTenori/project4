from flask import Flask, render_template
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "cookbook"
app.config['MONGO_URI'] = "mongodb://admin:verysecret12@ds241012.mlab.com:41012/cookbook"

mongo = PyMongo(app)
@app.route('/')
def index():
    return render_template('index.html', recipies = mongo.db.recipies.find())


if __name__ == '__main__':
    app.run(host = os.getenv('IP', '0.0.0.0'),
            port = os.getenv('PORT', '8080'),
            debug = True
            )