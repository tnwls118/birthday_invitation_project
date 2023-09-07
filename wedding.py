from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)


@app.route('/write', methods=['post'])
def write():
    name = request.form.get('name')
    content = request.form.get('content')

    mongo.db['happy'].insert_one({
        "name": name,
        "content": content
    })

    return redirect('/')


@app.route('/')
def run():
    now = datetime.datetime.now()
    dday = datetime.datetime(2023, 9, 29, 13, 0, 0)
    diff = (dday - now).days

    textbook = mongo.db['happy'].find()

    return render_template('/html.html', diff=diff, textbook=textbook)


app.run()
