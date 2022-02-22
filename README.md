# The FreeFrom CookBook

The FreeFrom CookBook is an online recipe book specifically catering for those with food allergies and intollerances. Last year I was diagnosed with a severe gluten-intollerance. Understanding free-from cooking, scrutinising labels and educating friends and family has quickly become part of my everyday life. I wanted to create a site where people could explore, create and share allergen free recipes in one place and help educate and promote the importance of understanding food allergies and intollerances. Food allergies can be isolating and stressful, so I wanted to create something with a community-feel and help make free-from cooking easier.

The FreeFrom CookBook has been developed for my Backend Development Milestone 3 Project, as part of my Full Stack Software Development Diploma with Code Insitute. 

Deployed site can be viewed [here](https://the-freefrom-cookbook.herokuapp.com/)

## Table of Contents

## Project Goals
- To promote understanding of food allergies and intollerances
- To create a site where users can easily access information and recipes, in addition to creating and saving their own.
- To build a mobile-first responsive site that can be accessed across all devices.
- To display information in user-friendly way, contributing to an overall good user experience.

## UX Design

## Strategy Plane

### Site owner Goals
* To share allergen free recipes
* To promote allergen free recipes
* To highlight and promote importance of understanding allergens
* To encourage users to create an account
* To encourage users to create recipes for the website


### User Stories

As first-time or casual user (as someone who has not registered):
* As a user I want to be able to understand the purpose of the site easily.
* As a user I want to be able to navigate throughout the site with ease.
* As a user I want to experience good responsive design, so I can access the site on different devices.
* As a user I want to enjoy stylish, clean design and style that is inline with the subject of the site.
* As a user I want a variety of recipes for different meals of the day.
* As a user I want to search for allergen specific recipes.
* As a user I want to be able to view recipes without having to create an account.
* As a user I want the option to register for an account, if I want to return later.

As a returning or registered user:
* As a user I want to log into my account.
* As a user I want to be able to delete my account.
* As a user I want to save recipes to my profile.
* As a user I want to create my own recipes.
* As a user I want to edit the recipes I have added.
* As a user I want to delete the recipes I have added.
* As a user I want to save ingredients to my shopping list.
* As a user I want to delete ingredients from my shopping list.
* As a user I want to sign up for a newsletter, so I can stay informed about new recipes.
* As a user I want to find social media links, so I can follow them on different platforms.
* As a user I want to contact admin with queries or feedback.
* As a user I want to find pagination on the recipe pages, so I do not experience endless scrolling.
* As a user I want to leave comments on recipes, so I can share my opinion with other users.

As admin:
* As admin I want to edit existing recipes created by any user.
* As admin I want to add new recipes.
* As admin I want to delete existing recipes created by any user.


## Scope Plane

### **Existing Features**
1. Design
    - Simple, clean design and layout with consistency throughout.
    - Easy navigation by using navigation bar
    - Responsive design allowing users to use site across all devices
2. Recipes
    - Recipes can be created, read, updated and deleted (CRUD) by the users.
    - Users of the site, either logged in or not, can search the recipes either by text input and/or filtering what allergens they want the recipe to be free from.
    - Logged in users can favourite recipes and save them to their profile.
    - Logged in users can save ingredients from recipe pages to their "shopping list" on their profile.
    - Logged in users have access to their profile, where they can view favourite recipes, recipes they uploaded and saved ingredients to their shopping list.
    - Recipe information includes servings, prep and cook times, what allergens it is free from, category, ingredients and the method.
    - Flash messages will appear when users create, edit, delete and favourite recipes and when their shopping list has been updated.
3. Register, Login and Logout
    - Users of the site can create an account.
    - Users can login into their existing account.
    - Users can logout of their account.
    - When a user logs in, logs out or creates a new account a flash message will display informing the user what has been actioned.
4. Contact and Newsletter
    - Users can contact the site owner through a contact form
    - Contact form powered by emailJS
    - On successfull delivery of a contact message, a modal will display informing the user it has been successful.
    - Users can sign up to a newsletter subscription
    - A flash message will display informing user either if subscription has been successful or if the email address already exists in database.

### **Features Left to Implement**
- A section on users home page of recipe suggestions based on type of recipes saved and created in their profile.
- Users to have ability to edit account, including changing password.
- Recipes to display a rating on recipe card based on the average ratings given.

## Structure Plane

## Skeleton Plane

### Wireframes

- [Home Page](static/images/readme_images/wireframes/home_page.png)
- [About Page](static/images/readme_images/wireframes/about_page.png)
- [Recipe Search Page](static/images/readme_images/wireframes/recipes.png)
- [Recipe Page](static/images/readme_images/wireframes/view_recipe.png)
- [Create Recipe Page](static/images/readme_images/wireframes/create_recipe.png)
- [Edit Recipe Page](static/images/readme_images/wireframes/edit_recipe.png)
- [Login Page](static/images/readme_images/wireframes/login.png)
- [Register Page](static/images/readme_images/wireframes/register.png)
- [Contact Page](static/images/readme_images/wireframes/contact_page.png)
- [User Profile Page](static/images/readme_images/wireframes/user_profile.png)
- [User Profile Favourite Recipes Page](static/images/readme_images/wireframes/user_profile_favourites.png)
- [User Profile Own Recipes Page](static/images/readme_images/wireframes/user_profile_recipes.png)
- [User Profile Shopping List Page](static/images/readme_images/wireframes/user_profile_shopping.png)

### Changes to Wireframes

## Surface Plane

### Colour Scheme
During development I explored different colour palettes and options. I wanted to use a colour scheme that was both pleasing to the using, and contributed to an overall stylish and simple design. Using [Coolors](https://coolors.co/), a colour palette was chosen. 

Initially this palette was chosen:
![Colour palette](static/images/readme_images/original_coolors.png)

After further exploration and development these colours were chosen:

![Image of pink colour](static/images/readme_images/colour_pink.png)
![Image of gray colour](static/images/readme_images/colour_gray.png)
![Image of blue colour](static/images/readme_images/colour_blue.png)
![Image of liver colour](static/images/readme_images/colour_liver.png)


### Images

The images in the site have been selected to showcase delcious, inviting free-from food. The site consists of a hero image on the Home page, an image displaying examples of food intollerances on the About Page and each recipe image. If the user does not upload an image, an image is provided. Images have been used from [Pexels](https://www.pexels.com/) and [Shutterstock](https://www.shutterstock.com/).

### Typography
[Google Fonts](https://fonts.google.com/) was used to choose fonts for the site. Lobster was chosen as the brand logo font, with its flowing, cursive design. Roboto Condensed was chosen for the rest of the site, as it is clear and easy to read. 

## Technologies

### Languages and Libraries
- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)- Flask dependency and used security helpers.
- [MongoDb](https://www.mongodb.com/) used to store database.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) Micro framework for building applications.
- [Jinga](https://jinja.palletsprojects.com/en/3.0.x/) was used as templating language for all pages throughout. 
- [jQuery](https://jquery.com/) was used for some Materialize elements.
- [Font Awesome](https://fontawesome.com/) was used for icons throughout the site.
- [Google Fonts](https://fonts.google.com/) was used to choose the fonts.
- [Materialize](https://materializecss.com/) was used for responsiveness, styling and elements such as forms, collapasible tables and tabs.

### IDE and Version Control
- [Git](https://git-scm.com/) was used for version control.
- [GitHub](https://github.com/) used for storing the project.
- [GitPod](https://www.gitpod.io/) was used for editing code.
- [Code Institute GitPod Template]() provided GitPod extensions.

### Design and Development
- [dbdiagram](https://dbdiagram.io/home) was used to create database schema diagram.
- [RandomKeygen](https://randomkeygen.com/) was used to generate secret key.
- [Balsamiq](https://balsamiq.com/) was used to create wireframes.
- [Coolors](https://coolors.co/) was used to help form a colour palette for the website.
- [Favicon](https://favicon.io/) was used to create a favicon for the site.

### Validating and Testing
- [Am I Responsive?](http://ami.responsivedesign.is/) used for creating mock ups.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) was used throughout development to troubleshoot and whilst testing.


## Testing

## Deployment

## Credits

### Code
- User Authentication and validating the Materialize select dropdown used from Code Institute's Task Manager mini project (Code Institute Task Manager)[https://github.com/Code-Institute-Solutions/TaskManagerAuth]
- Regex pattern for users to submit an image url used from (Stack Overflow)[https://stackoverflow.com/questions/169625/regex-to-check-if-valid-url-that-ends-in-jpg-png-or-gif/169631]
- Code for users to submit ingredients and method steps when creating a recipe and schema design was modified from (Wanderlust Recipes)[https://github.com/RussOakham/wanderlust-recipes]
- Pagination code used from (Sustainable Supper Club)[https://github.com/timmorrisdev/MS3-sustainable-supper-club/blob/main/app.py]
- (Pretty Pinted)[https://www.youtube.com/watch?v=_sgVt16Q4O4&ab_channel=PrettyPrinted] YouTube tutorial and code to capture checkbox activity into Flask.
- (SQL Server Guide)[https://sqlserverguides.com/mongodb-find-multiple-conditions/#:~:text=In%20Python%2C%20we%20can%20easily,use%20the%20find()%20method.] on MongoDb find multiple conditions to use multiple conditions in the search function.
- (Pocket Bookcase)[https://github.com/natalie-kate/pocket-bookcase] for help with profile function and contact form modal.
- (Stack Overflow)[https://stackoverflow.com/questions/6382023/changing-the-color-of-an-hr-element] used to style horizontal lines.
- (Materialize)[https://materializecss.com/] used for styling and responsiveness throughout including card panels, tabs and collapsibles.
- (Stack Overflow)[https://stackoverflow.com/questions/386281/how-to-implement-select-all-check-box-in-html] for help to create select all functionality on checkbox lists for both create and remove shopping list items.
- (Stack Overflow)[https://stackoverflow.com/questions/43076209/changing-materialize-css-navbar-active-color] used to help remove the background colour in Materialize active class on the navbar.


### Content
Recipes added by the developer/ admin are a mixture of their own recipes, modified and used from various sites, as shown below:
- (BBC Good Food)[https://www.bbcgoodfood.com/]
- (Two Pease and their Pod)[https://www.twopeasandtheirpod.com/]
- (Tesco)[https://realfood.tesco.com/]

Content about allergens from:
- (Foods Standards Agency)[https://www.food.gov.uk/sites/default/files/media/document/top-allergy-types.pdf]
- (Allergy UK)[https://www.allergyuk.org/types-of-allergies/food-allergy/]


### Media

#### Images
- Image on About page from (Shutterstock)[https://www.shutterstock.com/image-photo/balanced-diet-cooking-culinary-food-concept-300553067]
- Recipe images used to start the database used from (Pexels)[https://www.pexels.com/]
- Image used when user does not upload an image used from (Pexels)[https://www.pexels.com/photo/person-holding-sliced-vegetable-2284166/]
- Hero image used from (Pexels)[https://www.pexels.com/photo/red-and-white-round-fruits-on-brown-wooden-bowl-4099237/]


## Acknowledgements