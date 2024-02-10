"""
capybara_request.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape capybara subreddits:
reddit_collect("capybara+capybaras+capybarasoncritters", "capybara_request", "./instant-serotonin/data/capybara_data.p")
