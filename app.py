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
    recipes = mongo.db.recipes.find()
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

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)