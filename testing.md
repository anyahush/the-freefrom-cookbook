# Testing

## Code Validation

## User Stories
### User Stories

1. As a user I want to be able to understand the purpose of the site easily.
    * The landing page greets users with a welcome message introducing the site. The site name 'The FreeFrom Cookbook' is also displayed on the home page, in the navbar.

    ![Landing page with welcome messgae](static/images/readme_images/testing/user_stories/intro_message.png)

2. As a user I want to be able to navigate throughout the site with ease.
    * The navbar is accessible throughout the site, with clearly named links. 
    * The navbar options change depending on whether a user is logged in or not. 
    * The navbar changes to a sidenav on smaller screens.
    * Each page is clearly named with relevant headings at the top of each page.
    * There are buttons throughout the site that allow users to perform certain actions, these are labelled with label elements or tooltips.

    ![Navbar](static/images/readme_images/testing/user_stories/navbar.png)

3. As a user I want to experience good responsive design, so I can access the site on different devices.
    * The site has been developed to be enjoyed on all screen sizes.

    ![Recipe page on mobile screen size](static/images/readme_images/testing/user_stories/mobile_view.png)

4. As a user I want to enjoy stylish, clean design and style that is inline with the subject of the site.
    * The design of the site is minimal and stylish, using two key colours and utilising whitespace on the site. 
    * The design is user friendly and contributes to a good user experience.

    ![Landing Page](static/images/readme_images/testing/user_stories/landing_page.png)

5. As a user I want a variety of recipes for different meals of the day.
    * An initial library of recipes are available to users that have been created by Admin. All logged in users are able to create recipes that will add to the overall library.

    ![Recipe library](static/images/readme_images/testing/user_stories/recipe_library.png)

6. As a user I want to search for allergen specific recipes.
    * The search bar allows users to either search with a text input and/or selecting what allergens they wish the recipe to be free from.

    ![Search bar](static/images/readme_images/testing/user_stories/search_bar.png)

7. As a user I want to be able to view recipes without having to create an account.
    * All recipes are available to be viewed by all users, logged in or not.

8. As a user I want the option to register for an account, if I want to return later.
    * The option to register is available to all users that are not logged in at that moment. The register page is clearly labelled in the navbar.

    ![Register page](static/images/readme_images/testing/user_stories/register.png)

9. As a user I want to log into my account.
    * Users that have an existing account can select the login page and login into their account. 

    ![Login page](static/images/readme_images/testing/user_stories/login.png)

10. As a user I want to be able to delete my account.
    * On a user's profile there is a button, 'Delete Account', that allows users to delete their own account. A confirmation modal will pop up first, confirming the user wishes to delete their account.

    ![User profile intro](static/images/readme_images/testing/user_stories/user_profile.png)

11. As a user I want to save recipes to my favourites on my profile.
    * Logged in users, that did not create the recipe, can select the 'Add to favourites' button on either the recipe card in the recipe library on when viewing an individual recipe. 

    ![Favourite button on individual recipe page](static/images/readme_images/testing/user_stories/favourite_btn.png) 

    ![Favourite button on recipe card in library](static/images/readme_images/testing/user_stories/favourite_view_btn.png)

12. As a user I want to create my own recipes.
    * On a user's profile there is a button, 'Create recipe', that allows logged in users to create their own recipe.

13. As a user I want to edit the recipes I have added.
    * On recipes that a user has created the option to edit is available.
    * On the individual recipe view an 'Edit' button is displayed, allowing users that created the recipe to make changes.

    ![Action buttons for edit and delete](static/images/readme_images/testing/user_stories/action_buttons.png)

14. As a user I want to delete the recipes I have added.
    * On recipes that a user has created the option to delete the recipe is available.
    * On the individual recipe view a 'Delete' button is displayed, allowing users that created the recipe to delete it. 
    * A confirmation modal will pop up, confirming that the user wishes to delete their recipe.

    ![Confirmation modal](static/images/readme_images/testing/user_stories/confirmation_modal.png)

15. As a user I want to save ingredients to my shopping list.
    * For logged in users, ingredients can be selected and added to their 'Shopping List' on their profile, by selecting 'Save to Shopping List' button.

    ![Add ingredients to shopping list](static/images/readme_images/testing/user_stories/add_ingredients.png)

16. As a user I want to delete ingredients from my shopping list.
    * On a user's profile their 'Shopping List' is displayed. Users can select the ingredients they want to remove and select 'Remove ingredients'.

    ![Remove ingredients from shopping list](static/images/readme_images/testing/user_stories/shopping_list.png)

17. As a user I want to sign up for a newsletter, so I can stay informed about new recipes.
    * In the footer, available to all users, there is an option to sign up for a newsletter.
    * Users input their email, if they have already signed up it will flash saying already signed up.

    ![Newsletter signup](static/images/readme_images/testing/user_stories/newsletter_sign_up.png)

18. As a user I want to find social media links, so I can follow them on different platforms.
    * In the footer social media links are displayed to all users. These allow users to click on the link and it opens in a seperate tab.

    ![Social media links](static/images/readme_images/testing/user_stories/social_media_links.png)

19. As a user I want to contact admin with queries or feedback.
    * The contact page is available to all users, logged in or not. The contact form allows users to send a message to Admin.
    * The contact form is pre-populated with Name and Email for logged in users.

    ![Contact form](static/images/readme_images/testing/user_stories/contact_form.png)

20. As a user I want to find pagination on the recipe pages, so I do not experience endless scrolling.
    * On the recipe library and when users search for a recipe, pagination has been implemented.

    ![Pagination buttons](static/images/readme_images/testing/user_stories/pagination_buttons.png)

21. As a user I want to leave comments on recipes, so I can share my opinion with other users.
    * Logged in users can leave comments on recipes. All comments are viewed by all users.

    ![User comment section](static/images/readme_images/testing/user_stories/user_comments.png)

22. As a user, I want to leave a rating on a recipe.
    * Logged in users can rate a recipe out of 5 and it is displayed as a star rating in the comments section.

    ![Star rating in commments](static/images/readme_images/testing/user_stories/star_rating.png)

22. As admin I want to edit existing recipes created by any user.
    * Admin user is able to edit any recipe by any user. The 'Edit' button is displayed to Admin on all individual recipe pages.

    ![Admin action buttons](static/images/readme_images/testing/user_stories/admin_buttons.png)

23. As admin I want to add new recipes.
    * Admin is able to create new recipes by selecting, 'Create recipe' button on their profile.

24. As admin I want to delete existing recipes created by any user.
    * Admin user is able to delete any recipe by any user. The 'Delete' button is displayed to Admin on all individual recipe pages.

## Responsiveness

## Browser Compatibility

## Performance

[Google Chrome Lighthouse]() was used to test performance of all pages.

- Home page
![Home Page](static/images/readme_images/testing/home_page_performance.png)

- About Page
![About Page](static/images/readme_images/testing/about_page_performance.png)

- Recipes Library
![Recipes Library](static/images/readme_images/testing/recipe_library_performance.png)

- Individual Recipe Page
![Indvidual Recipe Page]()

- Profile Page
![Profile Page]()

- Contact Page
![Contact Page](static/images/readme_images/testing/contact_page_performance.png)

- Register Page
![Register Page]()

- Login Page
![Login Page]()

## Bugs