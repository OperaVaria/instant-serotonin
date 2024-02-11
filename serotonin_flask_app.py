"""
serotonin_flask_app.py

Main file of the "Instant Serotonin" project.

Flask app that collects and displays a random
cute/meme animal picture/gif upon website loading.
Current options: capybara, manul, sandcat, hedgehog.
Pictures sourced from subreddits.

By OperaVaria, 2024.
"""

# Flask imports:
from flask import Flask, flash, render_template, request, session
from flask_session import Session

# Built-in imports:
import pickle
from datetime import timedelta
from random import choice

# Create Flask app:
app = Flask(__name__)

# Set up session:
app.config['SECRET_KEY'] = "7dUP6J^n@dyNgQ"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=24)
app.config["SESSION_COOKIE_SECURE"] = True
sess = Session(app)


def load_from_pickle(file_path, exception_list):
    """Function to get random post from pickled list
       with a post exception list:"""
    with open(file_path, "rb") as file:
        sub_list = pickle.load(file)
    # This line looks horrendous but it is the quickest way
    # to remove items from a list which are present in another.
    post = choice(list(set(sub_list) - set(exception_list)))
    return post


# Page building decorators:
@app.route("/", methods=["GET", "POST"])
def index():
    """Set up index page."""
    # If redirected here from reset button POST request:
    # Reset exception list.
    # Display alert box.
    if request.method == "POST":
        session["except_pool"] = []
        alert = True
    else:
        alert = False
    return render_template("index.html", alert_flag=alert)

@app.route("/<animal>")
def result(animal):
    """Set up result page."""
    if animal in ("capybara", "hedgehog", "manul", "sand_cat"):
        # Setup for title variable.
        animal_name = str.title(animal.replace("_", " "))
        # Set up session exception list if not existent.
        if "except_pool" not in session:
            session["except_pool"] = []
        # Load post from pickled list, excluding except_pool. If out of posts,
        # display error page.
        try:    
            post = load_from_pickle(f"./data/{animal}_data.p",
                                    session.get("except_pool"))
        except IndexError:
            return render_template("error.html", title_var=animal_name,
                                   error_message=f"Out of {animal_name}s for today!",
                                   error_type="out_of_posts")
        # Append current post to exception list.
        session["except_pool"].append(post)
        # Render results page with proper variables.
        return render_template("result.html", title_var=animal_name, post_pic=post.url,
                           post_title=post.title, post_location="r/" + post.subreddit.display_name,
                           post_uploader=post.author)
    # If URL for animal does not exist, display error message:
    else:
        return render_template("error.html", error_message="No such Page!", error_type="no_url")


# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
