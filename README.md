![The Odd Blog](/readme-documents/odd-dog-header.png)

The Odd Dog Blog is a project for enthusiasts of all things dog shaped. Through the use of the MongoDB atlas database users will be able to start discussions of varying categories.
They will also be able to like, comment on, edit and delete said discussions. The database will also contain varying articles which the user can access from the home
page. The website is a multi-faceted website using flask template technology. The three pages are the index page, which contains blogs and articles. The discussions page, where
people can start discussions on a variation of categories. And the news page which has dog-related news-articles.

## UX

This website will be created for lovers of dogs and all things furry. The site users will be individuals with a passion for pets, 
dog owners looking for tips or advice or those who just want to brighten their day!

- As a user I can see what the main focus of the website is.
- As a user I can navigate through the website efficiently without questioning how to return.
![Navbar](/readme-documents/navbar.png)
- As a user I will be able to view an array of different blogs and articles.
![Article](/readme-documents/doggin-you.png)
- As a user I will be able to view any social media the company has.
![Socials](/readme-documents/socials.png)
- As a user I will be able to start a discussion of varying categories.
![Discussions](/readme-documents/discussions.png)
- As a user I will be able to search individual categories.
![Select Discussion](/readme-documents/select-discussion.png)
- As a user I will be able to like, edit, and delete discussions.
![Like, Edit, Delete](/readme-documents/like-edit.png)
- As a user I will be able to view the discussions thread.
![Discussion Thread](/readme-documents/d-thread.png)
- As a user I will be able to comment on a discussion.
![Comment, Like, Edit, Delete](/readme-documents/like-edit.png)
- As a user I will be able to like, edit and delete comments.
![Comments Like, Edit, Delete](/readme-documents/comment-like-edit.png)
- As a user I will be able to view news stories on the news page.
![Comments Like, Edit, Delete](/readme-documents/news.png)
- As a user I will able to view the website in a range of screen sizes.
![Responsive Sizes](/readme-documents/responsive-sizes.png)

My wireframes were made using [Balsamic](https://balsamiq.com/). You can view them [here](/wireframes/the-odd-dog-wires.pdf)

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

HTML5 is a markup language used for structuring and presenting content on the World Wide Web.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language like HTML.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.

- [J. Query (3.4.1)](https://jquery.com/download/)

jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax.

- [Google Fonts](https://fonts.google.com/)

Google Fonts (previously called Google Web Fonts) is a library of 991 free licensed font families, an interactive web directory for browsing the library,
and APIs for conveniently using the fonts via CSS[1] and Android.

- [Bootstrap (4.4.1)](https://getbootstrap.com/)

An open source toolkit for developing with HTML, CSS, and JS.

- [Font Awesome (V5.6.3)](https://fontawesome.com/)

A toolkit for icons.

- [Python](https://www.python.org/)

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, 
Python's design philosophy emphasizes code readability with its notable use of significant whitespace.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 
It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. 

- [Flask](https://www.mongodb.com/)

https://en.wikipedia.org/wiki/MongoDB

## Testing

- Having written my code for my .html page I have validated it on [The W3C Markup validation service](https://validator.w3.org/).

- I have validated my css on [Jigsaw](https://jigsaw.w3.org/css-validator/).

- My Python has been tested using [Pep8online](http://pep8online.com/).

This website was tested across multiple browsers (Chrome, Safari, Firefox and Microsoft edge.) It is also responsive,
having tested it on chrome developer tools across ipad, various iphones, samsungs etc. I have also tested it on iphone x, iphone 7, macbook and desktop.

### User stories Testing

- As a user I will be able to search different artists.

I have been through each individual artist and checked that there is the correct bio,
photo, albums and social links and these are responsive on all platforms.

- As a user I can see a small discography of the artist with spotify links to the artists music.

I have checked if each album link goes to the correct album on spotify by clicking upon each link.

- As a user I can navigate myself to any social media the artist has.

I have checked that each social media link goes to the correct artists social media account by clicking on each of the links.
I acknowledge that the artist Kojey Radical's twitter link is not correct. I believe the API has the incorrect information.

### Problems Encountered

During the project I encountered some small problems,

- The first problem I had was how to put multiple album covers and album links into a div using a for loop.
  I solved this by placing the elements into a variable first, but the next problem was that the new variable output some text stating undefined at the beginning of the variables.
  I removed this text with another variable then placed the variable into the div.

- Another problem I encountered was while viewing my website on my mobile, the description texts of the artists weren't so clear.
  I hadn't experienced this problem in chrome developer tools. It must be something involving screen resolution so I adjusted the font weight.

- I also witnessed some problems with image scalability when recieving artist images from the API's which I found relatively difficult to adjust.
  I overcame the problem with zoom and media queries.

- On the iphone 5/SE on developer tools I discovered that my texts for one artist was overflowing it's div.
  I adjusted the font sizes in media queries for this sized screen.

## Deployment

This site is hosted by GitHub pages deployed directly from the master branch. To deploy the website you must first go to your repository on
GitHub pages. You then click on settings, scroll down to GitHub pages. Select 'master branch' in source, then after a couple of minutes your website
will be deployed. You can then follow the link given in the GitHub pages section (https://theonorris.github.io/UK-Stand-Up/)

![GitHub pages example](/readme-documents/github-pages-example.png)

**To run locally you can clone this repository directly into the editor of your choice by firstly,**

- copying the link from clone or download on my GitHub page.

![git copy](/readme-documents/gitclone-example.png)

- then, pasting git clone https://github.com/TheoNorris/UK-Stand-Up.git into your terminal.

![git clone](/readme-documents/gitclone.png)

- To cut ties with this GitHub repository, type `git remote rm origin`into the terminal.

![git remove](/readme-documents/git-remove.png)

## Credits

### content and media

Most of the Rap history was taken from [wikipedia](https://en.wikipedia.org/wiki/British_hip_hop#:~:text=The%20first%20UK%20record%20label,acts%20was%20founded%20in%201986.&text=Music%20of%20Life%20was%20swiftly,through%20in%20his%20vocal%20style.),
besides small parts being written by me. The Photo of London on the main page is by [Pierre Blaché](https://www.instagram.com/pierre9x6/) taken from [pexels](https://www.pexels.com/).
The artists bio's are taken from the [last.fm API](https://www.last.fm/api/). While the artists photos, album covers, names and social links are taken from the [happi API](https://happi.dev/docs/music).

### Acknowledgements

A thank you to [Cormac](https://github.com/armedcor), my tutor and [Precious](https://github.com/precious-ijege), my mentor for their continual help throughout the project.
