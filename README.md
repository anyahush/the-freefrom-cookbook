# The FreeFrom CookBook
Insert introduction
Insert deployed link here

## Table of Contents

## Project Goals


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
* As a user I want a to search for allergen specific recipes.
* As a user I want to be able to view recipes without having to create an account.
* As a user I want the option to register for an account, if I want to return later.

As a returning or registered user:
* As a user I want to log into my account.
* As a user I want to edit my account, including password and personal details.
* As a user I want to be able to delete my account.
* As a user I want to save recipes to my profile.
* As a user I want to create my own recipes.
* As a user I want to edit the recipes I have added.
* As a user I want to delete the recipes I have added.
* As a user I want to save ingredients to my shopping list.
* As a user I want to sign up for a newsletter, so I can stay informed about new recipes.
* As a user I want to find social media links, so I can follow them on different platforms.
* As a user I want to contact admin with queries or feedback.
* As a user I want to find pagination on the recipe pages, so I do not experience endless scrolling.

As admin:
* As admin I want to edit existing meal type categories.
* As admin I want to add meal type categories.
* As admin I want to delete existing meal type categories.
* As admin I want to edit existing recipes.
* As admin I want to add new recipes.
* As admin I want to delete existing recipes.
* As admin I want to be able to delete a user.
* As admin I want to be able to reset user passwords if users have trouble logging in.
* As admin I want to be able to give another user admin rights. 



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

### Typography
[Google Fonts](https://fonts.google.com/) was used to choose fonts for the site. Lobster was chosen as the brand logo font, with its flowing, cursive design. Roboto Condensed was chosen for the rest of the site, as it is clear and easy to read. 

## Technologies

### Languages

- HTML
- CSS3
- JavaScript

### Frameworks and Libraries
- [Coolors](https://coolors.co/) was used to help form a colour palette for the website.
- [Google Fonts](https://fonts.google.com/) was used to choose the fonts.

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
- Hero image used from (Pexels)[https://www.pexels.com/photo/red-and-white-round-fruits-on-brown-wooden-bowl-4099237/]


## Acknowledgements