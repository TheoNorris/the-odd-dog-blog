![The Odd Blog](/readme-files/readme-documents/odd-dog-header.png)

The Odd Dog Blog is a project for enthusiasts of all things dog shaped. Through the use of the MongoDB atlas database, users will be able to start discussions of varying categories.
They will also be able to like, comment on, edit and delete said discussions. The database will also contain varying articles which the user can access from the home
page. The website is a multi-faceted website using flask template technology. The three main pages are the index page, which contains blogs and articles. The discussions page, where
people can start discussions on a variation of categories. And the news page which has dog-related news-articles.

## UX

This website will be created for lovers of dogs and all things furry. The site users will be individuals with a passion for pets, 
dog owners looking for tips or advice or those who just want to brighten their day!

- As a user I can see what the main focus of the website is.

- As a user I can navigate through the website efficiently without questioning how to return.

![Navbar](/readme-files/readme-documents/navbar.png)

- As a user I will be able to view an array of different blogs and articles.

![Article](/readme-files/readme-documents/doggin-you.png)

- As a user I will be able to view any social media the company has.

![Socials](/readme-files/readme-documents/socials.png)

- As a user I will be able to start a discussion of varying categories.

![Discussions](/readme-files/readme-documents/discussions.png)

- As a user I will be able to search individual categories.

![Select Discussion](/readme-files/readme-documents/select-discussion.png)

- As a user I will be able to like, edit, and delete discussions.

![Like, Edit, Delete](/readme-files/readme-documents/like-edit.png)

- As a user I will be able to view the discussions thread.

![Discussion Thread](/readme-files/readme-documents/d-thread.png)

- As a user I will be able to comment on a discussion.

![Comment, Like, Edit, Delete](/readme-files/readme-documents/like-edit.png)

- As a user I will be able to like, edit and delete comments.

![Comments Like, Edit, Delete](/readme-files/readme-documents/comment-like-edit.png)

- As a user I will be able to view news stories on the news page.

![Comments Like, Edit, Delete](/readme-files/readme-documents/news.png)

- As a user I will able to view the website in a range of screen sizes.

![Responsive Sizes](/readme-files/readme-documents/responsive-sizes.png)

My wireframes were made using [Balsamic](https://balsamiq.com/). You can view them [here](/readme-files/wireframes/the-odd-dog-blog-wires.pdf)

## Schema

My Database is divided into four sections. 

- The first and most simple is categories. This is just the four categories that users can select to
start a discussion.

![Schema Categories](/readme-files/readme-documents/schema-categories.png)

- The second manages articles and blog posts on the main page.

![Schema Articles](/readme-files/readme-documents/schema-articles.png)

- The third database contains users discussions accompanied by the category, date, time, user and the amount of likes they have on their comment. I have also added a 
can't delete boolean to some of the articles as there is no user authentication. This way all the discussions will not to be deleted.

![Schema Articles](/readme-files/readme-documents/schema-discussions.png)

- The fourth database contains discussions thread comments. Comments that a user has added to a discussion. This database contains a comment_id which is an
id that matches the object_id of the particular comment the user has commented on in the discussion database. It also contains the user, date, time and if anyone has liked this
comment.

![Schema Articles](/readme-files/readme-documents/schema-discussions-thread.png)

## Existing Features

- Social links to the company's social media.
- A database of blogs and articles, accessible to the user on selection.
- A discussions page where the user can start discussions, like, edit or delete discussions
- A discussions thread where the user can comment on existing discussions. These comments can also be liked, edited or deleted.
- A news page with collapsible articles.
- A select bar where users can select from a category of discussions.

### Features left to implement

- In the future I would like to implement user authentication. In the time-frame I had, I did not find this was possible.

- I will implement a comments section for the blog and article posts.

- I would like to add a reviews section also in which I can sell or have links to the best products on the market.


## technologies used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

    - HTML5 is a markup language used for structuring and presenting content on the World Wide Web.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

    - Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

    - JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.

- [J. Query (3.4.1)](https://jquery.com/download/)

    - jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax.

- [Google Fonts](https://fonts.google.com/)

    - Google Fonts (previously called Google Web Fonts) is a library of 991 free licensed font families, an interactive web directory for browsing the library,
      and APIs for conveniently using the fonts via CSS[1] and Android.

- [Bootstrap (4.4.1)](https://getbootstrap.com/)

    - An open source toolkit for developing with HTML, CSS, and JS.

- [Font Awesome (V5.6.3)](https://fontawesome.com/)

    - A toolkit for icons.

- [Python](https://www.python.org/)

    - Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, 
      Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

    - Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 
     It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. 

- [MongoDB](https://www.mongodb.com/)

    - MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL).

## Testing

- Having written my code for my .html page I have validated it on [The W3C Markup validation service](https://validator.w3.org/).

- I have validated my css on [Jigsaw](https://jigsaw.w3.org/css-validator/).

- My Python has been tested using [Pep8online](http://pep8online.com/).

This website was tested across multiple browsers (Chrome, Safari, Firefox and Microsoft edge.) It is also responsive,
having tested it on chrome developer tools across ipad, various iphones, samsungs etc. I have also tested it on iphone x, iphone 7, macbook and desktop.

### User stories Testing

- As a user I can see what the main focus of the website is.

This is apparent in the name in the navbar.

- As a user I can navigate through the website efficiently without questioning how to return.

I have been through every link on the website, always being able to return to the home page if necessary. The navbar is also fixed so there is an option
to return whenever seen fit. The website also has a personalised 404 page with a home link so the user should never get lost.

- As a user I will be able to view an array of different blogs and articles.

I have clicked on each of the links to each of the articles and made sure that each link is going to the correct article and picture.

- As a user I will be able to view any social media the company has.

These are always visible in the footer of each page. I have clicked on each link to ensure they go to the correct platform in a new window.

- As a user I will be able to start a discussion of varying categories.

There are four different categories on the discussions page, in the 'start a discussion' modal. These are all apparent in the select bar. I have been through each category
and checked they work correctly. 
If a user has selected a category from the search discussions select bar, they are only able to start a discussion in the selected category, from the 'start a discussion modal' in that category.
I have been to the different categories and tested this. 
Either way of starting a discussion I have added validation. I have been through each input area and tested whether or not these areas need validation. I have started discussions and
ensured these discussions are posted correctly.

- As a user I will be able to search individual categories.

I have tested that the select discussion category goes to the correct category for each selection by clicking on each individual category. 

- As a user I will be able to like, edit, and delete discussions.

I have been to each page, pages being, discussions, edit_discussion and filtering and have checked that all these functions work correctly.
I have done this by clicking the like button, I have also edited and deleted discussions.

- As a user I will be able to view the discussions thread.

I have been to the discussions thread by clicking on comments. I have checked that the discussion and the comments are displayed correctly.

- As a user I will be able to comment on a discussion.

On the discussions thread there is a form to add comments, I have been through the form, checked that the validation is working correctly and submitted the form.
On submission the comment pops up above the form. This displays the form is working correctly.

- As a user I will be able to like, edit and delete comments.

I have been to each page, pages being, discussions_thread and edit_reply and have checked that all these functions work correctly.
I have done this by clicking the like button, I have also edited and deleted discussions. I acknowledge that on the edit_reply page you are returned to the discussions page, not the correct discussions_thread when the 
comment is edited. This is because the discussions_thread has a particular object id in it's address and I had difficulty entering it into the redirect route from update_reply.

- As a user I will be able to view news stories on the news page.

I have been to the news page and checked each news story. I have checked that the collapsible function is working effectively and that the news story is matching the correct headline.

- As a user I will able to view the website in a range of screen sizes.

I have been through the whole range of views on the chrome developer tools ensuring that the apllication looks just as stylish and modern on each size. I have also viewed the application
on laptop, desktop and a variation of phones.

### Problems Encountered

During the project I encountered some small problems,

- The first problem was I couldn't have two loops on the same html page for the same category.

    - I solved this by splitting categories into it's own database. This way I was able to have two loops in the same form.

- The second problem I encountered was having form submission on a modal
  
    - I looked to stack overflow for this problem as people before me had faced the same issue. Here I found the code I needed to make this modal function
      correctly.

- The biggest problem which consumed most of my time on this project was being able to edit and delete comments which were made on a discussion.

    - I overcame this issue by seperating my discussion_thread comments to a different database. This was a great lesson in database structure because once I had done this
      I could make the function work almost instantaneously.

- The next issue I had difficulty with was pagination. My tutor, Cormac helped me with this and this was very important to learn. Once you understand the structure it is very straight
forward.

- I currently have one existing problem which is the submit button in edit_reply.

    - When a user submits the edit_reply form they are directed to the discussions page. This is not the correct page they should be directed to. They should be directed back to the 
      discussions_thread. I had a lot of difficulty with this because the discussions thread also has an object id in it's address. I found it challenging to formulate a way to redirect the page
      back to the the discussions thread from the update_reply route.

- A small issue I currently have is that I could not implement a validation modal on the comment remove button in the discussions thread.

    - When I implemented one and selected remove, it removed the first comment instead of the selected one. I believe this is because it was not registering to the loop I had in place to display and
    alter the comments. The modal worked perfectly well on the discussions page and I even attempted to clone the same piece of code. I was very pushed for time as I had already started the next module of the course
    so in the future I believe this issue will be solvable.

## Deployment

This site is hosted on Heroku deployed directly from the master branch. To deploy the website you must first create a Heroku account.

- Next you will create an app on Heroku

![Creat Heroku App](/readme-files/readme-documents/heroku-create-app.png)

-After this you will want to add your configuration variables. You can do this inside settings of your Heroku app. You want to add IP address, Port, and your 
environment variables of the application. In this case my variable examples are stored in my env_sample.py file. You will have to create your own based on the examples of what
you need. I would highly recommend you store your environment variables in their own file which is ignored when being push to a server.

![Configuration variables](/readme-files/readme-documents/environment-variables.png)

- You will need to ensure you have a Procfile. You do this by entering the following into the bash terminal.

![Procfile](/readme-files/readme-documents/procfile.png)

- You will also need a requirements.txt file.

![Requirements.txt](/readme-files/readme-documents/requirements.png)

- git add . and git commit with a meaningful commit

![Git Commit](/readme-files/readme-documents/git-commit.png)

- Once these requirements are done you can login to your Heroku in the bash terminal.

![Heroku Login](/readme-files/readme-documents/heroku-login.png)

- Next push the application to heroku using.

![Heroku push](/readme-files/readme-documents/git-push.png)

- Finally command Heroku to start running the application 

![Heroku Run](/readme-files/readme-documents/heroku-run.png)

- Now, inside Your Heroku dashboard in the top right of the window you can now open the the application.

![Open App](/readme-files/readme-documents/open-app.png)

**To run locally you can clone this repository directly into the editor of your choice by firstly,**

- copying the link from clone or download on my [GitHub page](https://github.com/TheoNorris/the-odd-dog-blog).

![git copy](/readme-files/readme-documents/git-clone-example.png)

- then, pasting git clone https://github.com/TheoNorris/the-odd-dog-blog.git into your terminal.

![git clone](/readme-files/readme-documents/git-clone.png)

- To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

![git remove](/readme-files/readme-documents/git-remove.png)

- Upon using this project you will need to use your own environment variables. You can see an example
of the variables I have used in my env_sample.py file. Before you host this project, ensure that you 
have ignored this file before pushing your project to the server.

![env vars](/readme-files/readme-documents/env-vars.png)

## Credits

### content and media

The news articles I have used on this website are copyright free and have been taken from [News USA](https://www.copyrightfreecontent.com/?s=dog+couch).
The photos were taken from [Pexels](https://www.pexels.com/) and a whole variation of photographers. [Jayson Lorenzo](https://www.instagram.com/iamjaysonlorenzo/), [Sergio Souza](https://www.pexels.com/@serjosoza), [Dominika Roseclay](https://www.instagram.com/dominika_roseclay/),
[Spencer Gurley](https://www.instagram.com/spencergurley/), [The Missin Lovers](https://www.instagram.com/missinlovers/), [Tom Verdoot](https://www.instagram.com/verdoottom/), [Dominic Buccilli](https://www.instagram.com/dombuccilli/), [Julissa Helmuth](https://www.instagram.com/httpx.jh/),
[Prime Photo](https://www.instagram.com/primephotos__/), [Nishizuka](https://www.pexels.com/@nishizuka-25426?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels), [Melchor Gama](https://www.instagram.com/MELCHOR_GAMA/), [Noelle Otto](https://www.instagram.com/noelle.grace/),
[Free stock photos](https://www.instagram.com/freestocks/), [Lisa Fotios](https://www.instagram.com/lisafotios/)

### Acknowledgements

A thank you to [Cormac](https://github.com/armedcor), my tutor and [Precious](https://github.com/precious-ijege), my mentor for their continual help throughout the project.
