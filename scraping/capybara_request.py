"""
capybara_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import Path class:
from pathlib import Path

# Import scraping function:
from reddit_scrape import reddit_collect

# Create an absolute path for output pickle file.
output_file = Path(__file__).parents[1].resolve() / "data/capybara_data.p"

# Scrape capybara subreddits:
reddit_collect("capybara+capybaras+capybarasoncritters", "capybara_request", output_file)
