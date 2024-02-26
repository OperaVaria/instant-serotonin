"""
manul_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import Path class:
from pathlib import Path

# Import scraping function:
from reddit_scrape import reddit_collect

# Create an absolute path for output pickle file.
output_file = Path(__file__).parents[1].resolve() / "data/manul_data.p"

# Scrape manul subreddits:
reddit_collect("PallasCats+manuls", "manul_request", output_file)
