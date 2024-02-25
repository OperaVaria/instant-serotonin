"""
serotonin_flask_app.py

Main file of the "Instant Serotonin" project.

Flask app that collects and displays a random
cute/meme animal picture/gif upon website loading.
Current options: capybara, manul, sandcat, hedgehog.
Pictures sourced from subreddits.

By OperaVaria, 2024.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@proton.me"
__version__ = "1.0.0"
__date__ = "2024.02.26"


# Licence:
__license__ = "GPLv3"
__copyright__ = "Copyright © 2024, Csaba Latosinszky"

"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>
"""

# Flask imports:
from flask import Flask, abort, render_template, request, session
from flask_session import Session

# Built-in imports:
import json
import pickle
from random import choice

# Create Flask app.
app = Flask(__name__)

# Flask app configuration:
app.config.from_file("./config/secretKey.json", load=json.load) # Load secret key.
app.config.from_pyfile("./config/settings.py") # Load other settings.

# Set up Session.
sess = Session(app)


def load_from_pickle(file_path, exception_list):
    """Function to get random post from pickled list
       with an exception list passed."""
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
    # Set alert box flag.
    if request.method == "POST":
        session["exceptPool"] = []
        alert = True
    else:
        alert = False
    return render_template("index.html", version=__version__, alert_flag=alert)

@app.route("/<animal>")
def result(animal):
    """Set up result page."""
    # If URL for animal does not exists, throw 404.
    if animal not in ("capybara", "hedgehog", "manul", "sand_cat"):
        abort(404)
    # Set up animal strings.
    animal_var = animal.replace("_", " ")
    animal_title = str.title(animal_var)
    # Set up session exception list, if non-existent.
    if "exceptPool" not in session:
        session["exceptPool"] = []
    # Load post from pickled list, excluding exceptPool. If out of posts,
    # display error page.
    try:
        post = load_from_pickle(f"./data/{animal}_data.p",
                                session.get("exceptPool"))
    except IndexError:
        return render_template("no-post.html", title_var=animal_title,
                            error_message=f"Out of {animal_var}s for today!",
                            version=__version__)
    # Append current post to exception list.
    session["exceptPool"].append(post)
    # Render results page with proper variables.
    return render_template("result.html", title_var=animal_title, post_pic=post.url,
                    post_title=post.title, post_location="r/" + post.subreddit.display_name,
                    post_uploader=post.author, version=__version__)


# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
