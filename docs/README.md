# Instant Serotonin

This is the source code for a simple webapp that scrapes the internet for cute/meme
animal pictures/gifs, and displays one at random upon user request.
The app is mainly written in Python, utilising the Flask web framework.
The frontend part is a standard HTML-CCS-JS website, with a simple custom styling.

## Functionality

The webapp, in its current form, is set up to be hosted at [pythonanywhere.com](https://www.pythonanywhere.com/).
Scheduled background tasks (the scripts in ./scraping/) collect the top 30 "hot" posts from preset subreddits every night,
and store the information in pickle files (./data/). The raw data is then read when Flask assembles the requested HTML page,
and a random post is selected.

Server-side Flask sessions are utilised (via the Flask-Session extension) to avoid duplicate results for the same user.

The HTML-CSS side has a responsive, Flexbox layout. It is optimized to display correctly on all
screen types.

## Screenshots

![screenshot_1](assets/images/main.jpg "main.html")

![screenshot_1](assets/images/capybara.jpg "capybara.html")

![screenshot_1](assets/images/sand_cat.jpg "sand_cat.html")

## Other

The currently running version is accessible: **[here](https://serotonin-operavaria.eu.pythonanywhere.com/)**.

Sources of the static images used in this project: **[image_sources.md](image_sources.md)**.

**[Contact](mailto:lcs_it@proton.me)**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
