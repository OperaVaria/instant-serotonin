"""
hedgehog_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape hedgehog subreddits:
reddit_collect("Hedgehog+Hedgehogs+HedgehogsAreLiquid", "hedgehog_request", "./instant-serotonin/data/hedgehog_data.p")
