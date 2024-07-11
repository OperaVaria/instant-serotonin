"""
serotonin_flask_app.py

Main file of the "Instant Serotonin" project.

Flask app that collects and displays a random
cute/meme animal picture/gif upon request.
Current options: capybara, manul, sandcat, hedgehog.
Pictures sourced from Pexels, Pixabay, Reddit and Unsplash.

By OperaVaria, 2024.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@proton.me"
__version__ = "2.0.1"
__date__ = "2024.03.28"


# Licence:
__license__ = "GPLv3"
__copyright__ = "Copyright © 2024, Csaba Latosinszky"

"""
This program is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/>
"""

# Built-in imports:
import json
import pickle
from datetime import datetime
from pathlib import Path
from random import choice

# Flask imports:
from flask import Flask, abort, render_template, request, send_from_directory, session
from werkzeug.utils import secure_filename

# Import Flask extensions:
from flask_minify import Minify
from flask_session import Session
from flask_talisman import Talisman

# Import setting variables:
from config.settings import csp  # Content security policy settings.
from config.settings import bypass  # Minify bypass settings.

# Create path constants.
PROJECT_DIR_PATH = Path(__file__).parents[0].resolve()
CONFIG_DIR_PATH = (PROJECT_DIR_PATH).joinpath("config/")
DATA_DIR_PATH = (PROJECT_DIR_PATH).joinpath("data/")
SECRET_KEY_PATH = (CONFIG_DIR_PATH).joinpath("secretKey.json")
SETTINGS_FILE_PATH = (CONFIG_DIR_PATH).joinpath("settings.py")

# Create Flask app.
app = Flask(__name__)

# Flask app configuration:
app.config.from_file(SECRET_KEY_PATH, load=json.load) # Load secret key.
app.config.from_pyfile(SETTINGS_FILE_PATH) # Load other settings.

# Set up Talisman. Force HTTPS should normally be on, but Cloudflare handles it.
tali = Talisman(app, content_security_policy=csp, force_https=False)

# Set up Minify.
mini = Minify(app=app, bypass=bypass, html=True, js=True, cssless=True)

# Set up Session.
sess = Session(app)

# Current year variable for footer.
current_year = datetime.now().year


def load_from_pickle(file_path, exception_list):
    """Function to get random post from pickled list
       with an exception list passed."""
    with open(file_path, "rb") as file:
        pickled_list = pickle.load(file)
    # This line looks horrendous but it is the quickest way
    # to remove items from a list which are present in another.
    post = choice(list(set(pickled_list) - set(exception_list)))
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
    return render_template("index.html", current_year=current_year,
                           version=__version__, alert_flag=alert)

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
    # Create secure pickle file path, load post from pickled list, excluding exceptPool.
    # If out of posts, display error page.
    file_name = secure_filename(f"{animal}_data.p")
    pickle_file_path = (DATA_DIR_PATH).joinpath(file_name)
    try:
        post = load_from_pickle(pickle_file_path, session.get("exceptPool"))
    except IndexError:
        return render_template("no-post.html", current_year=current_year, title_var=animal_title,
                               animal_var=animal_var, version=__version__)
    # Append current post to exception list.
    session["exceptPool"].append(post)
    # Render results page with proper variables.
    return render_template("result.html", current_year=current_year,
                           title_var=animal_title, post=post, version=__version__)

@app.route("/robots.txt")
def robots_txt():
    """Set up robots.txt."""
    return send_from_directory("static", "other/robots.txt")

@app.route("/humans.txt")
def humans_txt():
    """Set up humans.txt."""
    return send_from_directory("static", "other/humans.txt")

@app.route("/sitemap.xml")
def sitemap_xml():
    """Set up sitemap.xml."""
    return send_from_directory("static", "other/sitemap.xml")


# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
