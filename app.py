import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env 

app = Flask(__name__)

app.config["MONGODB_NAME"] = "odd_dog"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/discussions')
def discussions():
    all_categories = mongo.db.categories.find()
    comments = mongo.db.comments.find()
    return render_template('health.html', comments=comments, 
                           now=datetime.now().strftime("%D, %H:%M"),
                           categories=all_categories)


@app.route('/health')
def health():
    image = url_for('static', filename='images/yorkshire-terrier.jpg')
    comments = mongo.db.comments.find({'category_name': 'Health'})
    return render_template('health.html', comments=comments, image=image)


@app.route('/lifestyle')
def lifestyle():
    image = url_for('static', filename='images/man-with-dog.jpg')
    comments = mongo.db.comments.find({'category_name': 'Lifestyle'})
    return render_template('health.html', comments=comments, image=image)


@app.route('/story')
def story():
    image = url_for('static', filename='images/dog-gang.jpg')
    comments = mongo.db.comments.find({'category_name': 'Story'})
    return render_template('health.html', comments=comments, image=image)


@app.route('/food')
def food():
    image = url_for('static', filename='images/black-and-white-dalmatian.jpg')
    comments = mongo.db.comments.find({'category_name': 'Food'})
    return render_template('health.html', comments=comments, image=image)

@app.route('/goodboy')
def goodboy():
    return render_template('goodboy.html')

@app.route('/badbreath')
def badbreath():
    return render_template('badbreath.html')

@app.route('/chewed_couch')
def chewed_couch():
    return render_template('chewed_couch.html')

@app.route('/newpuppy')
def newpuppy():
    return render_template('newpuppy.html')

@app.route('/better_life')
def better_life():
    return render_template('better_life.html')

@app.route('/dog_bathing')
def dog_bathing():
    return render_template('dog_bathing.html')

@app.route('/pet_allergies')
def pet_allergies():
    return render_template('pet_allergies.html')


@app.route('/start_discussion')
def start_discussion():
    return render_template('start_discussion.html', 
                           now=datetime.now().strftime("%D, %H:%M"), 
                           categories=mongo.db.categories.find())


@app.route('/insert_discussion', methods=['POST'])
def insert_discussion():
    comments = mongo.db.comments
    comments.insert_one(request.form.to_dict())
    return redirect(url_for('discussions'))


@app.route('/edit_discussion/<comment_id>')
def edit_discussion(comment_id):
    the_comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_discussion.html', 
                           now=datetime.now().strftime("%D, %H:%M"), 
                           comment=the_comment, categories=all_categories)


@app.route('/update_discussion/<comment_id>', methods=["POST"])
def update_discussion(comment_id):
    comments = mongo.db.comments
    comments.update({'_id': ObjectId(comment_id)},
                    {
                     'category_name': request.form.get('category_name'),
                     'date_time': request.form.get('date_time'),
                     'username': request.form.get('username'),
                     'title': request.form.get('title'),
                     'comment': request.form.get('comment'),
                     'likes': request.form.get('likes'),
                    })
    return redirect(url_for('discussions'))


@app.route('/update_likes/<comment_id>', methods=["POST"])
def update_likes(comment_id):
    comments = mongo.db.comments
    comments.find_one_and_update({'_id': ObjectId(comment_id)},
                                 {
                                  '$inc': {'likes': 1},
                                 })
    return redirect(url_for('discussions'))


@app.route('/delete_discussion/<comment_id>')
def delete_discussion(comment_id):
    mongo.db.comments.remove({'_id': ObjectId(comment_id)})
    return redirect(url_for('discussions'))


@app.route('/add_comment/<comment_id>')
def add_comment(comment_id):
    the_comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    return render_template('add_comment.html',
                           now=datetime.now().strftime("%D, %H:%M"),
                           comment=the_comment)


@app.route('/reply/<comment_id>', methods=["POST"])
def reply(comment_id):
    comments = mongo.db.comments
    comments.update({'_id': ObjectId(comment_id)},
                    {
                      '$push': {'comments': {
                                             'date_time':
                                             request.form.get('date_time'),
                                             'username':
                                             request.form.get('username'),
                                             'comment':
                                             request.form.get('comment'),
                                            }}
                     })
    return redirect(request.referrer)


@app.route('/edit_reply/<comment_id>, <reply_comment>')
def edit_reply(comment_id, reply_comment):
    the_reply = mongo.db.comments.find_one({'_id': ObjectId(comment_id),
                                            "comments": reply_comment})
    return render_template('edit_reply.html',
                           now=datetime.now().strftime("%D, %H:%M"),
                           reply=the_reply)


@app.route('/update_reply/<reply_comment>', methods=["POST"])
def update_reply(reply_comment):
    comments = mongo.db.comments
    comments.update({'comments': reply_comment},
                    {
                     '$push': {'comments': {
                                             'date_time':
                                             request.form.get('date_time'),
                                             'username':
                                             request.form.get('username'),
                                             'comment':
                                             request.form.get('comment'),
                                            }}
                    })
    return redirect(url_for('discussions'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
