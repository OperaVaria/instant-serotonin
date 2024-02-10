"""
sandcat_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape sand cat subreddit:
reddit_collect("sandcats", "sand_cat_request", "./instant-serotonin/data/scdata.p")
