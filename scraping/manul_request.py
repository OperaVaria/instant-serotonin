"""
manul_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape manul subreddits:
reddit_collect("PallasCats+manuls", "manul_request", "./instant-serotonin/data/manul_data.p")
