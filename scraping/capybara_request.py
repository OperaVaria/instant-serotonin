# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape capybara subreddit:
reddit_collect("capybara+capybaras+capybarasoncritters", "capybara_request", "./instant-serotonin/data/capydata.p")
