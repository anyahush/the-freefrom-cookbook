import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


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

@app.route("/get_recipes")
def get_recipes():
    """
    Gets recipes from db and displays 
    """
    recipes = list(mongo.db.recipes.find())
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template(
        "recipes.html", recipes=recipes, allergens=allergens)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Creates search function, so users can search recipe db for
    specific recipes or ingredients
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)

@app.route("/register", methods=["GET", "POST"])
def register():
    """ register view, when form submitted database
    is updated
    """
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
        flash("Registration is successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allows users to login into an existing account and verifies 
    username and password
    """
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
    """
    Displays user profile once logged in
    """
    # get user's username from database
    user = mongo.db.users.find_one(
        {"username": username})

    if user['username'] == session['user']:
        recipes = list(mongo.db.recipes.find(
            {"created_by": username}))
        favourites = list(mongo.db.profiles.find(
            {"favourites": username}
        ))
        return render_template(
            "profile.html", username=username,
            recipes=recipes, favourites=favourites)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Allows users to logout of account
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    """
    Displays selected recipe in seperate page 
    based on recipe_title
    """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    """
    Allow users to create a recipe and save
    """
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
    categories = mongo.db.categories.find().sort("category_name", 1)
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template(
        "create_recipe.html", categories=categories, allergens=allergens)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """ Allow users to edit existing recipe """
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

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    allergens = mongo.db.allergens.find().sort("allergen_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe,
        categories=categories, allergens=allergens)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """ Users can delete their own recipes from the db """
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("get_recipes"))


@app.route("/favourite_recipe/<recipe_id>")
def favourite_recipe(recipe_id):
    """ Users can save recipes to their profile """
    username = mongo.db.users.find_one(
        {"username": username})

    if "user" in session:
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        mongo.db.profiles.update_one({"_id": ObjectId(username)}, {
                "$push": {"favourites": recipe}})
        flash("Recipe successfully added!")
        return redirect(url_for(
            "view_recipe", recipe_id=recipe_id))

@app.route("/create_shopping_list/<recipe_id>", methods=["GET", "POST"])
def create_shopping_list(recipe_id):
    """ Users can select ingredients to save to own profile """
    if "user" in session:

        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

        if request.method == "POST":
            update_list = {
                shopping_list: request.form.getlist("shopping_list")
            }

            update = mongo.db.profiles.insert_one(
                {"user_id": ObjectId(user_id)},
                {"$addToSet": {"own_shopping_list": update_list}})

            if update:
                flash("Shopping List Saved")
                return redirect("get_recipes")


@app.route("/shopping_list", methods=["GET", "POST"])
def shopping_list():
    """ Dislays users saved shopping items """

    return render_template("profile.html")


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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)