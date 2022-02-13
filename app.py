import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

#configurations
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

def paginated(recipes):
    PER_PAGE = 6
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    PER_PAGE = 6
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(
        page=page, per_page=PER_PAGE, total=total, css_framework="materialize")

@app.route("/")
def index():
    """
    Displays the home page
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """ Displays content to user about the site """

    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template("about.html", allergens=allergens)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/get_recipes")
def get_recipes():
    """ Gets recipes from db and displays """
    recipes = list(mongo.db.recipes.find())
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)

    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)

    return render_template(
        "recipes.html", recipes=recipes_paginated,
        pagination=pagination, allergens=allergens)


@app.route("/search", methods=["GET", "POST"])
def search():
    """ Creates search function based on input and/
    or checkboxes selected """

    if request.method == "POST":
        # get search bar input
        query = request.form.get("query")
        # get allergen checkboxes selected
        allergen_query = request.form.getlist("allergen-query")

        # if input and checkbox filled in
        if query and allergen_query:
            recipe_results = list(mongo.db.recipes.find({
                "$and": [
                    {"allergen_list": {"$in": allergen_query}},
                    {"$text": {"$search": query}}]
            }))
            if recipe_results:
                recipes_paginated = paginated(recipe_results)
                pagination = pagination_args(recipe_results)
        # if just search input
        elif query:
            recipe_results = list(mongo.db.recipes.find(
                {"$text": {"$search": query}}))
            if recipe_results:
                recipes_paginated = paginated(recipe_results)
                pagination = pagination_args(recipe_results)
        # if just checkbox selected
        elif allergen_query:
            recipe_results = list(mongo.db.recipes.find(
                {"allergen_list": {"$in": allergen_query}}))
            if recipe_results:
                recipes_paginated = paginated(recipe_results)
                pagination = pagination_args(recipe_results)

        return render_template("recipes.html",
            recipes=recipes_paginated, pagination=pagination)

# users
@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register view, when form submitted database
    is updated """

    if request.method == "POST":
        # checks if username is already taken
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # if username is taken, message displayed and reloads page
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get("password") != request.form.get(
                "confirm-password"):
            # checks if confirmed password matches original password
            # If confirmation
            # not met, flash message displayed and reloads page
            flash("Your password did not match, please try again")
            return redirect(url_for("register"))
        
        register_user = {
            # gets user information from registration form
            "username": request.form.get("username").lower(),
            "first-name": request.form.get("first-name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            "admin": bool("")
        }
        # new user created in db
        mongo.db.users.insert_one(register_user)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        mongo.db.profiles.insert_one({
            "user_id": ObjectId(user_id),
            "favourites": [],
            "shopping_list": []})
        
        name = request.form.get("first_name")
        flash(f'Welcome {name}' +
            'you have been successfully registered.')
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Allows users to login into an existing account and verifies 
    username and password """

    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}". format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # if password does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ Displays user profile once logged in """

    # only users can view profile
    if "user" in session:
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        user = mongo.db.users.find_one(
            {"username": session["user"]}["username"]
        )
        user_profile = mongo.db.profiles.find_one(
            {"user_id": ObjectId(user_id)})
        recipes = list(mongo.db.recipes.find(
            {"created_by": username}))
        favourites = user_profile["favourites"]
        shopping_list = user_profile["shopping_list"]
 
        return render_template(
            "profile.html",
            recipes=recipes, favourites=favourites,
            shopping_list=shopping_list, username=username)
    
    else:
        flash("You need to be signed in for that")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """ Allows users to logout of account """

    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    """ Displays selected recipe in seperate page 
    based on recipe_title """
    # find recipe in db by id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # if recipe not found show error
    if not recipe:
        return render_template("404.html")

    return render_template("view_recipe.html", recipe=recipe)


# recipes
@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    """ Allow users to create a recipe and save """

    # only users can create recipe
    if not session.get("user"):
        return render_template("404.html")

    # add recipe to db
    if request.method == "POST":
        recipe = {
            "recipe_title": request.form.get("recipe_title"),
            "category_name": request.form.get("category_name"),
            "image_url": request.form.get("image_url"),
            "allergen_list": request.form.getlist("allergen_list"),
            "servings": request.form.get("servings"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "recipe_description": request.form.get("recipe_description"),
            "ingredients": request.form.getlist("ingredients"),
            "method_step": request.form.getlist("method_step"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Task successfully added")
        return redirect(url_for("get_recipes"))
    # find catergories and allergen list from db
    categories = mongo.db.categories.find().sort("category_name", 1)
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template(
        "create_recipe.html", categories=categories, allergens=allergens)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """ Allow users to edit existing recipe """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # only users that created the recipe can edit the recipe
    if session.get("user") == recipe["created_by"]:

        # edit recipe and update db
        if request.method == "POST":
            edit = {
                "recipe_title": request.form.get("recipe_title"),
                "category_name": request.form.get("category_name"),
                "image_url": request.form.get("image_url"),
                "allergen_list": request.form.getlist("allergen_list"),
                "servings": request.form.get("servings"),
                "prep_time": request.form.get("prep_time"),
                "cook_time": request.form.get("cook_time"),
                "recipe_description": request.form.get("recipe_description"),
                "ingredients": request.form.getlist("ingredients"),
                "method_step": request.form.getlist("method_step"),
                "created_by": session["user"]
            }
            mongo.db.recipes.replace_one({"_id": ObjectId(recipe_id)}, edit, True)
            flash("Recipe successfully updated")
    else:
        return render_template("404.html")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe,
        categories=categories, allergens=allergens)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """ Users can delete their own recipes from the db """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # only users that created the recipe can delete it
    if session.get("user") == recipe["created_by"]:
        mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
        flash("Recipe successfully deleted")
        return redirect(url_for("get_recipes"))
    else:
        return render_template("404.html")


@app.route("/favourite_recipe/<recipe_id>")
def favourite_recipe(recipe_id):
    """ Users can save recipes to their profile """
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    favourites = mongo.db.profiles.find_one(
        {"user_id": ObjectId(user_id)})["favourites"]
    user_profile = mongo.db.profiles.find_one(
        {"user_id": ObjectId(user_id)})

    if "user" in session:

        mongo.db.profiles.update_one(
            {"user_id": ObjectId(user_id)},
            {"$addToSet": {"favourites": recipe}})
        flash("Recipe successfully added!")
        return redirect(url_for(
            "view_recipe", recipe_id=recipe_id, favourites=favourites))

@app.route("/create_shopping_list/<recipe_id>", methods=["GET", "POST"])
def create_shopping_list(recipe_id):
    """ Users can select ingredients to save to own profile """
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    user_profile = mongo.db.profiles.find_one(
        {"user_id": ObjectId(user_id)})

    if "user" in session:

        if request.method == "POST":
            shopping_list = request.form.getlist('shopping_list')
            
            update = mongo.db.profiles.update_one(
                {"user_id": ObjectId(user_id)},
                {"$addToSet": {"shopping_list": shopping_list}})
            
            if update:
                flash("Shopping List Saved")
                return redirect(url_for(
                    "view_recipe", recipe_id=recipe_id))



@app.route("/create_comment/<recipe_id>", methods=["GET", "POST"])
def create_comment(recipe_id):
    """ Logged in users can leave a comment on a recipe """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if request.method == "POST":
        comment = {
            "comment": request.form.get("user_comment"),
            "author": session["user"]
        }

        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)},
            {"$push": {"comments": comment}})
        flash("Comment successfully added")
        return redirect(url_for("view_recipe", recipe_id=recipe_id))
    return render_template("view_recipe", comment=comment)


# error handlers
@app.errorhandler(404)
def page_not_found(error):
    """ 404 error handling from flask documentation """
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(error):
    """ 500 error handling from flask documentation """
    return render_template("500.html"), 500

# run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)