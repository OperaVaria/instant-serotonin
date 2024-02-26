"""
sandcat_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import Path class:
from pathlib import Path

# Import scraping function:
from reddit_scrape import reddit_collect

# Create an absolute path for output pickle file.
output_file = Path(__file__).parents[1].resolve() / "data/sand_cat_data.p"

# Scrape sand cat subreddit:
reddit_collect("sandcats", "sand_cat_request", output_file)
