# Import libraries for Python.
import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env 

app = Flask(__name__)

# Configurations For PyMongo.
app.config["MONGODB_NAME"] = "odd_dog"
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# Route or index page.
@app.route('/')
def index():
    return render_template('index.html')



# Route that receives a category from my search bar in my navbar and searches 
# for the specific category for the filtering.html page.
@app.route('/health')
def health():
    image = url_for('static', filename='images/yorkshire-terrier.jpg')
    comments = mongo.db.comments.find({'category_name': 'Health'})
    return render_template('filtering.html', comments=comments, image=image)


# Route that receives a category from my search bar in my navbar and searches 
# for the specific category for the filtering.html page.
@app.route('/lifestyle')
def lifestyle():
    image = url_for('static', filename='images/man-with-dog.jpg')
    comments = mongo.db.comments.find({'category_name': 'Lifestyle'})
    return render_template('filtering.html', comments=comments, image=image)


# Route that receives a category from my search bar in my navbar and searches
# for the specific category for the filtering.html page.
@app.route('/story')
def story():
    image = url_for('static', filename='images/dog-gang.jpg')
    comments = mongo.db.comments.find({'category_name': 'Story'})
    return render_template('filtering.html', comments=comments, image=image)


# # Route that receives a category from my search bar in my navbar and searches 
# for the specific category for the filtering.html page.
@app.route('/food')
def food():
    image = url_for('static', filename='images/black-and-white-dalmatian.jpg')
    comments = mongo.db.comments.find({'category_name': 'Food'})
    return render_template('filtering.html', comments=comments, image=image)

# Route to find and import specific blogpost for my blogposts.html page when 
# someone selects an article on the index.html page.
@app.route('/goodboy')
def goodboy():
    image = url_for('static', filename='images/man-training-a-rottweiler.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     'How to turn a bad pooch into a good boy.'})
    return render_template('blogpost.html', 
                           blog_articles=blog_articles, image=image)


# Route to find and import specific blogpost for my blogposts.html page when 
# someone selects an article on the index.html page.
@app.route('/badbreath')
def badbreath():
    image = url_for('static', 
                    filename='images/english-bulldog.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     "Is your dogs bad breath doggin' you?"})
    return render_template('blogpost.html', 
                           blog_articles=blog_articles, image=image)


# Route to find and import specific blogpost for my blogposts.html page when 
# someone selects an article on the index.html page.
@app.route('/chewed_couch')
def chewed_couch():
    image = url_for('static', filename='images/shih-tzu.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     'Put a stop to the chewed up couch.'})
    return render_template('blogpost.html', blog_articles=
                           blog_articles, image=image)


# Route to find and import specific article for my articles.html when someone selects an article on the index.html page.
@app.route('/newpuppy')
def newpuppy():
    image = url_for('static', filename='images/puppy-sleeping.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     'Are you ready for a new puppy?'})
    return render_template('articles.html', 
                           blog_articles=blog_articles, image=image)


# Route to find and import specific article for my articles.html when someone selects an article on the index.html page.
@app.route('/better_life')
def better_life():
    image = url_for('static', filename='images/siberian-husky.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     'Four tips for a better life.'})
    return render_template('articles.html', 
                           blog_articles=blog_articles, image=image)


# Route to find and import specific article for my articles.html when someone selects an article on the index.html page.
@app.route('/dog_bathing')
def dog_bathing():
    image = url_for('static', filename='images/chihuahua.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     'Tips for easier dog bathing.'})
    return render_template('articles.html', 
                           blog_articles=blog_articles, image=image)


# Route to find and import specific article for my articles.html when someone selects an article on the index.html page.
@app.route('/pet_allergies')
def pet_allergies():
    image = url_for('static', filename='images/portuguese-water-dog.jpg')
    blog_articles = mongo.db.blog_articles.find_one({'blog_title': 
                                                     '6 Myths About Pet Allergies.'})
    return render_template('articles.html', blog_articles=blog_articles, 
                           image=image)


# Route for my news html page.
@app.route('/news')
def news():
    return render_template('news.html')


# Route that finds and imports all my discussion starters/comments for my 
# discussions.html page.
@app.route('/discussions')
def discussions():
    all_categories = mongo.db.categories.find()
    comments = mongo.db.comments.find()
    return render_template('discussions.html', comments=comments, 
                           now=datetime.now().strftime("%D, %H:%M"),
                           categories=all_categories)


# Route that receives a new discussion from my modal on my discussions.html 
# then inserts it into my MongoDB comments library
@app.route('/insert_discussion', methods=['POST'])
def insert_discussion():
    comments = mongo.db.comments
    comments.insert_one(request.form.to_dict())
    return redirect(url_for('discussions'))


# Route that renders my edit.html and finds the correct discussion comment 
# to edit from my comments library. The comment to edit has been selected on 
# the discussions.html and it's id has been passed into the edit route.
# I also pass in the date and time from datetime.
@app.route('/edit_discussion/<comment_id>')
def edit_discussion(comment_id):
    the_comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_discussion.html', 
                           now=datetime.now().strftime("%D, %H:%M"), 
                           comment=the_comment, categories=all_categories)


# Route that updates a comment using the comment id passed in from edit.html. 
# It then gets the form information from my edit.html form.
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

# Route adds likes to the comments database on the specific comment, from the 
# like button on the discussions.html page.
@app.route('/update_likes/<comment_id>', methods=["POST"])
def update_likes(comment_id):
    comments = mongo.db.comments
    comments.find_one_and_update({'_id': ObjectId(comment_id)},
                                 {
                                  '$inc': {'likes': 1},
                                 })
    return redirect(url_for('discussions'))

# Route deletes specific comment from the database that the user has selected 
# on discussions.html.
@app.route('/delete_discussion/<comment_id>')
def delete_discussion(comment_id):
    mongo.db.comments.remove({'_id': ObjectId(comment_id)})
    return redirect(url_for('discussions'))


# Route creates discussions thread.html. It is passed in the comment id from 
# discussions.html when the user clicks on comment. The page displays the 
# comment the user wants to reply on and the comments that have been made on 
# the discussion comment. These are received from the comments and comment 
# replies libraries using the comment id for both.
@app.route('/discussions_thread/<comment_id>')
def discussions_thread(comment_id):
    the_comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    reply_comment = mongo.db.comment_replies.find({'comment_id': comment_id})
    return render_template('discussions_thread.html',
                           now=datetime.now().strftime("%D, %H:%M"),
                           comment=the_comment,
                           reply_comment=reply_comment)


# Route inserts new reply to discussion comment into the comment_replies 
# database. The comment id of the discussion comment is passed in from the 
# discussions_thread.html and this is used as 'comment_id' to locate the 
# correct reply for the specified discussion comment. The comment, date, 
# time and username are received from the form on the discussions_thread.html
@app.route('/reply/<comment_id>', methods=['POST'])
def reply(comment_id):
    comments = mongo.db.comment_replies
    comments.insert_one({ 
                         'comment_id': comment_id,
                         'date_time': request.form.get('date_time'),
                         'username': request.form.get('username'),
                         'comment': request.form.get('comment'),
                         })
    return redirect(request.referrer)


# Route for rendering edit_reply.html. The reply id is passed in from the 
# discussion_thread.html edit button. This is used to locate the reply in 
# order to edit the details in the form in edit.html. datetime is also passed
# in to the form
@app.route('/edit_reply/<reply_id>')
def edit_reply(reply_id):
    the_reply = mongo.db.comment_replies.find_one({'_id': ObjectId(reply_id)})
    return render_template('edit_reply.html',
                           now=datetime.now().strftime("%D, %H:%M"),
                           reply=the_reply)


#Route is used to update the edit of the reply. The reply id is passed into 
# the route from the edit.html form. This then locates the correct reply in 
# the comment_replies database and updates it using the information receieved 
# from the form in edit.html.
@app.route('/update_reply/<reply_id>', methods=["POST"])
def update_reply(reply_id):
    reply = mongo.db.comment_replies
    reply.update({'_id': ObjectId(reply_id)},
                 {
                  'comment_id': request.form.get('comment_id'),
                  'date_time': request.form.get('date_time'),
                  'username': request.form.get('username'),
                  'comment': request.form.get('comment'),
                 })
    return redirect(url_for('discussions'))


# Route that deletes reply comments. It receives the reply id from the remove 
# button in discussions_thread.html. It then locates said reply and removes it 
# from the database.
@app.route('/delete_reply/<reply_id>')
def delete_reply(reply_id):
    mongo.db.comment_replies.remove({'_id': ObjectId(reply_id)})
    return redirect(request.referrer)


# Route adds likes to the comment_replies datasbase on the specific comment, from the 
# like button on the discussions_thread.html page.
@app.route('/update_likes_for_reply/<reply_id>', methods=["POST"])
def update_likes_for_reply(reply_id):
    comments = mongo.db.comment_replies
    comments.find_one_and_update({'_id': ObjectId(reply_id)},
                                 {
                                  '$inc': {'likes': 1},
                                 })
    return redirect(request.referrer)


# If statement runs the application.
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
