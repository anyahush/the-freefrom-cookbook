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
@app.route("/get_recipes")
def get_recipes():
    """
    Gets recipes from db and displays 
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

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


@app.route("/index")
def index():
    """
    Displays the home page
    """
    return render_template("index.html")


@app.route("/recipes/<recipe_title>")
def recipe(recipe_title):
    """
    Displays selected recipe in seperate page 
    based on recipe_title
    """
    recipe_record = mongo.db.recipes.find_one({"url": recipe_title})

    if recipe_record:

        return render_template(
            "view-recipe.html",
            recipe=recipe_record)
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)