import itertools
import os
from datetime import datetime
from flask import Flask,render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env 

app = Flask(__name__)

app.config["MONGODB_NAME"] = "task_manager"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/discussions')
def discussions():
    return render_template('discussions.html',  comments=mongo.db.comments.find())

@app.route('/start_discussion')
def start_discussion():
    return render_template('start_discussion.html', now = datetime.now().strftime("%D, %H:%M"), comments=mongo.db.comments.find())

@app.route('/insert_discussion', methods=['POST'])
def insert_discussion():
    comments = mongo.db.comments
    comments.insert_one(request.FILES.form.to_dict())  
    return redirect(url_for('discussions'))

@app.route('/edit_discussion/<comments_id>')
def edit_discussion(comments_id):
    return render_template('edit_discussion.html', now = datetime.now().strftime("%D, %H:%M"), comments=mongo.db.comments.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)

