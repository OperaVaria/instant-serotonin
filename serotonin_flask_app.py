"""
Flask app that collects and displays a random
meme animal picture upon website loading.
Current options: capybara, manul.
Pictures sourced from subreddits.
"""

# Flask imports:
from flask import Flask, render_template

# Built-in imports:
import random
import pickle

# Declare Flask app:
app = Flask(__name__)


# Function to get random post from pickled list:
def load_from_pickle(file_path):
    with open(file_path, "rb") as file:
        sub_list = pickle.load(file)
    post = random.choice(sub_list)
    return post


# Page building decorators:
@app.route("/")
def index():
    """Set up index page."""
    return render_template("index.html", title_bar = "Instant Serotonin | Quick copium for everyone")

@app.route("/capybara")
def capybara():
    """Set up capybara page."""
    post = load_from_pickle("./data/capydata.p")
    return render_template("result.html", title_bar = "Instant Capybara | Quick copium for everyone",
                           page_title="Instant Capybara", post_pic=post.url, post_title=post.title,
                           post_location="r/capybara", post_uploader=post.author)

@app.route("/manul")
def manul():
    """Set up manul page."""
    post = load_from_pickle("./data/manuldata.p")
    return render_template("result.html", title_bar = "Instant Manul | Quick copium for everyone",
                           page_title="Instant Manul", post_pic=post.url, post_title=post.title,
                           post_location="r/PallasCats", post_uploader=post.author)

# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
