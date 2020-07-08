import os
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
    return render_template('discussions.html', comments=mongo.db.comments.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)

