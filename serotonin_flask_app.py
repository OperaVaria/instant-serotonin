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


@app.route("/")
def index():
    """Set up index.html"""
    return render_template("index.html", title_variable = "Instant Serotonin | Quick copium for everyone")

@app.route("/capybara")
def capybara():
    """Set up capybara.html"""
    with open("./instant-serotonin/data/capydata.p", "rb") as file:
        sub_list = pickle.load(file)
    post = random.choice(sub_list)
    return render_template("capybara.html", title_variable = "Instant Capybara | Quick copium for everyone",
                           capy_pic=post.url, capy_title=post.title, capy_uploader=post.author)

@app.route("/manul")
def manul():
    """Set up manul.html"""
    with open("./instant-serotonin/data/manuldata.p", "rb") as file:
        sub_list = pickle.load(file)
    post = random.choice(sub_list)
    return render_template("manul.html", title_variable = "Instant Manul | Quick copium for everyone",
                           manul_pic=post.url, manul_title=post.title, manul_uploader=post.author)

# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
