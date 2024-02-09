"""
Flask app that collects and displays a random
cute animal picture upon website loading.
Current options: capybara, manul, sandcat, hedgehog.
Pictures sourced from subreddits.

By OperaVaria, 2024.
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
    return render_template("index.html")

@app.route("/capybara")
def capybara():
    """Set up capybara page."""
    post = load_from_pickle("./data/capydata.p")
    return render_template("result.html", title_var="Capybara", post_pic=post.url,
                           post_title=post.title, post_location="r/" + post.subreddit.display_name,
                           post_uploader=post.author)

@app.route("/manul")
def manul():
    """Set up manul page."""
    post = load_from_pickle("./data/manuldata.p")
    return render_template("result.html", title_var="Manul", post_pic=post.url,
                           post_title=post.title, post_location="r/" + post.subreddit.display_name,
                           post_uploader=post.author)

@app.route("/sand_cat")
def sand_cat():
    """Set up sand cat page."""
    post = load_from_pickle("./data/scdata.p")
    return render_template("result.html", title_var="Sand Cat", post_pic=post.url,
                           post_title=post.title, post_location="r/" + post.subreddit.display_name,
                           post_uploader=post.author)

@app.route("/hedgehog")
def hedgehog():
    """Set up hedgehog page."""
    post = load_from_pickle("./data/hedgehdata.p")
    return render_template("result.html", title_var="Hedgehog", post_pic=post.url,
                           post_title=post.title, post_location="r/" + post.subreddit.display_name,
                           post_uploader=post.author)


# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
