# Testing

## Table of Contents
1. [Code Validation](#code-validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
2. [User Stories](#user-stories)
3. [Responsiveness](#responsiveness)
4. [Browser Compatability](#browser-compatibility)
5. [Performance](#performance)
6. [Manual Testing](#manual-testing)
7. [Bugs](#bugs)


## Code Validation

### HTML Validation
All HTML pages were tested using [W3C Markup Validation](https://validator.w3.org/). 
- URLs were passed through the validator to prevent errors appearing as Jinga Templating was used throughout.
-  For the profile page the URL did not work due to sensitive data. The page source on Google Chrome was used to test the code.
- One error is displayed on all pages. This refers to the section element that holds the flash messages.

![Example of HTML Validation](static/images/readme_images/testing/validation/html_validation_final.png)

### CSS Validation
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to test the style.css file. No changes were required.

![CSS Validation](static/images/readme_images/testing/validation/css_final.png)

### JavaScript Validation
[JSHint Validator](https://jshint.com/) was used to validate all JavaScript files. 

![JSHint final validation](static/images/readme_images/testing/validation/jshint_final.png)
![JSHint final validation contact page](static/images/readme_images/testing/validation/jshint_final_contact.png)


### Python Validation
[PEP8 Online](http://pep8online.com/) validator was used to test the app.py file.

![PEP8 online validation](static/images/readme_images/testing/validation/pep8_final.png)

## User Stories

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
The site was tested using [Mobile Compatitbility Tester - Google Mobile Friednly Test](https://search.google.com/test/mobile-friendly) and [Google Chrome Developer Tools](). 

The Mobile Compatibility tester returned good results for all pages that could be tested. Pages protecting user logins could not be tested using this site. Responsiveness testing was carried out using Chrome Dev tools. Additionally real world testing was carried out on my iphone13, macBook Pro and additional Lenovo PC screen. Below are the results from Chrome Dev tool testing.

![Site responsiveness table](static/images/readme_images/testing/responsiveness_table.png)

Whilst testing for responsiveness a bug was found.
    - On screen sizes of 1024px, the recipe cards on the recipes library were coming off the card panel and a vertical scroll was appearing. A media query has been added to prevent this and to display all information to the user without a scrollbar.

After fixing this error, The FreeFrom CookBook has no responsive design errors.

## Browser Compatibility
[Lambdatest](https://accounts.lambdatest.com/dashboard) was used to test browser compatability for the site. 

The following browsers were tested:
* Chrome 91 (Windows 10)- good
* Firefox 89 (Windows 10)- good
* Edge 91 (Windows 10)- good
* Opera 74 (Windows 10)- good
* Safari 12 (macOS Mojave)- good
* IE 11 (Windows 8.1)- issues

Additionally the site was developed using Google Chrome 98 on macOS Monterey and crosschecked with Safari 15.

All browswers, except IE, returned good results and displayed the site well.

There were compatability issues with IE:
* Rendering some of the images
* Displaying Materialize components such as the footer
* Keeping the responsive layout of the site.

## Performance

[Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test performance of all pages. Initially across the site alt attributes and amendment to header orders were added to improve Lighthouse performance scores. 

Overall the site performs well on desktop. For mobile devices the site performs well but has scored lower on performance, primarily due to large media content. Currently the site performs well but in the future may have issues if the database grows, which could affect app performance. Further development coudl include limits on image sizes on the URL and compressing the images on the server.

Below are the Lighthouse results:

<details>
<summary>Home page</summary>

* Mobile

![Home Page](static/images/readme_images/testing/home_performance_mobile.png)

* Desktop

![Home Page](static/images/readme_images/testing/home_performance.png)
</details>

<details>
<summary>About Page</summary>

* Mobile

![About Page](static/images/readme_images/testing/about_performance_mobile.png)

* Desktop 

![About Page](static/images/readme_images/testing/about_performance.png)
</details>

<details>
<summary>Recipes Library </summary>

* Mobile

![Recipes Library](static/images/readme_images/testing/recipe_library_mobile.png)

* Desktop

![Recipes Library](static/images/readme_images/testing/recipe_library_performance.png)
</details>

<details>
<summary>Individual Recipe Page</summary>

* Mobile

![Indvidual Recipe Page](static/images/readme_images/testing/recipe_page_performance_mobile.png)

* Desktop

![Indvidual Recipe Page](static/images/readme_images/testing/recipe_page_performance.png)
</details>

<details>
<summary>Profile Page </summary>

* Mobile

![Profile Page](static/images/readme_images/testing/profile_perfomance_mobile.png)

* Desktop

![Profile Page](static/images/readme_images/testing/profile_perfomance.png)
</details>

<details>
<summary>Contact Page </summary>

* Mobile

![Contact Page](static/images/readme_images/testing/contact_performance_mobile.png)

* Desktop

![Contact Page](static/images/readme_images/testing/contact_page_performance.png)
</details>

<details>
<summary>Register Page </summary>

* Mobile 

![Register Page](static/images/readme_images/testing/register_performance_mobile.png)

* Desktop

![Register Page](static/images/readme_images/testing/register_performance.png)
</details>

<details>
<summary>Login Page</summary>

* Mobile

![Login Page](static/images/readme_images/testing/login_performance_mobile.png)

* Desktop 

![Login Page](static/images/readme_images/testing/login_performance.png)
</details>

## Manual Testing
Throughout development manual testing was carried out, in addition to futher testing at the end of the project. Testing was carried out on Google Chrom 98 and Safari 15.1
- Nav links take user to relevant page
- Brand logo takes user back to the home page
- Email subscription input works and flash message appears
- Social media links open in a seperate tab to relevant site
- Search bar allows users to input word search and/ or select an allergen from drop down.
    * Reset button is required to be clicked in order to reset allergen drop down.
    * When users clicked more than one allergen to search for, the recipe results were showing all recipes that had a least one allergen listed in the free from section. The $in operator
    was changed to $all. This has resolved the isssue. Now users can search for multiple allergens and it will show recipes that are free from all of them.
    * When users clicked the search button without typing or selecting an allergen it was showing an unbound local error. A else statement was added to the search function, adding a flash message asking users to type or select and redirecting them back to the recipes library.
- Recipes library
    * Displays all recipes. Those logged in and did not create recipe can add recipe to favourites. This button works and flashes a messaged to the user.
- Recipe page
    * Add to favourites button and remove from favourites button works and flashes a message to the user.
    * Shopping list displayed, users can select an item, multiple or all and add to shopping list. This flashes to the user it has been successful.
    * A ::marker class was being displaying on the select all checkbox, making the checkbox sit to the right. The checkbox was taken out of the li element. This has removed the marker.
    * User comments section- users can't submit a comment without typing comment and selecting a rating. This prompts user if they don't select one or both when clicking submit.
    * For users that created the recipe, edit and delete buttons are displayed. Both work and flash messages once completed. A confirmation modal pops up before deleting a recipe, to prevent accidental deletion.
- About page
    * Displays all information
    * Materialize collapsible using dynamically generated information, works and allows users to expand information as when they wish.
- Profile page
    * All buttons work, and complete action that they are labelled to do
    * Delete account- confirmation modal pops up first, so users cannot accidentally delete their account.
- Shopping List
    * Whilst testing I discovered that a user could click 'Save to Shopping List' or 'Remove from Shopping List' and regardless if a user selected an ingredient it would flash saying it was successful.
    * A JavaScript function was added to check if the length of checked boxes is less than 1 and if so alert the user to select an ingredient. 
- Create Recipe
    * Form is validated throughout. Has labels and prompts were requried, to guide the user on how to fill the form out.
    * Image remains optional and image provided if user does not upload one
- Edit Recipe
    * On testing, once edited the site was redirecting users back to the recipes library. This has been fixed and takes users back to the recipe they just edited, so they can view their changes.
- Contact Form
    * Form is validated, including textarea validation preventing blank messages being sent
    * Form is pre-populated with user information if logged in
    * Personalised modal pop ups once form submitted
- Register Form
    * Form is validated, highlights to user what is required if not filled in correctly
    * Once registered takes user to profile and flashes welcome message
- Login Form
    * Exisitng users can log in
    * If successful, takes users to their profile and welcome message displayed
    * If unsuccessful a flash message will appear prompting users that password and or username is incorrect


## Bugs

### Found and Fixed
- Whilst developing, I wanted users to be able to add ingredients to their shopping list on their profile and then to delete selected ones. Initially users were able to select an ingredients(s) but it would delete all ingredients that had been added at the same time. I discovered I had been pushing the original ingredients as an array, rather than individual ingredients. Therefore with nested arrays, I was targeting the wrong object. I added the $each modifier to the $push operator, so that it pushed each ingredient into one array. Now users can remove an ingredient at a time, or select multiple.
- During development there were issues with Regex patterns that prevented blank messages or inputs being submitted. A correct Regex pattern was added to inputs and a JavaScript function added to prevent a blank message being sent on the contact form. 
- Through peer code review, additional padding to the email input for the newsletter subscription was suggested. This was added.
- Through peer code review, it was highlighted that when a user creates a recipe, it takes them back to the recipe library rather than viewing the recipe they just created. This was fixed by changing the return redirect to view_recipe and generating the recipe_id by using inserted_id.
- HTML validation errors:
    * An error displayed for the profile page saying that a div element had been used inside a list. 
    * This was changed to an li element.

![Example of Profile page validation](static/images/readme_images/testing/validation/html_errors.png)

- JavaScript validation errors:
    * On both files errors displayed due to the version of JavaScript being used. 
    * Unused variables were detected, this is due to jQuery being used to find variables and emailJS, which is an external API.
    * In contact.js, an unused variable was removed and missed semi-colon added.

![JSHint Validation](static/images/readme_images/testing/validation/jshint_errors.png)
![JSHint Validation Contact page](static/images/readme_images/testing/validation/jshint_errors_contact.png)

- Python validation errors:
    * Initially it came back with errors relating to trailing whitespace, lines too long and incorrect indentation. 
    * This was resolved and the validation came back with no errors.

![PEP8 online validation](static/images/readme_images/testing/validation/pep8_errors.png)

- Performance
    * Whilst testing performance I discovered that the hero image and image on the About page were causing performance issues due to their size. I subsequently used [Cloud Converter](https://cloudconvert.com/) to compress the images.
    * This has improved the performance of both pages on mobile and desktop.
    * Additionally, alt attributes were missed on some images and the order of header elements needed attention. These were fixed during testing.
- During final testing, I discovered there was a horizontal scroll on my individual recipe page. I use Google Chrome, so cross checked the site on multiple screen sizes and Safari. I used [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB), in additional to Chrome Developer Tools and couldn't find what was causing this. A peer also cross checked it on desktop, tablet and mobile screen sizes and the horizontal scroll was not there. I checked again and it has gone. I think it may have been an error in my browser. Currently as it is there is no horizontal scroll on the site.
- Just prior to submission, an error was displayed in the console as the deployed site could not find the favicon files. There had been no issues with this up until now. In order to remove concole errors, the favicon was removed. I had designed the favicon myself, using [Favicon](https://favicon.io/). I intend to add this in future development and explore why an error was now being displayed.

![Favicon image](static/images/readme_images/testing/favicon_bug.png)


### Existing
- Once users have searched once, in order to access allergen drop down list the reset button needs to be clicked. In future development, I intend to explore how to ensure that the drop down automatically refreshes without the user having to do so.