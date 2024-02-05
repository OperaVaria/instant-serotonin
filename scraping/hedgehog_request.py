# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape hedgehog subreddit:
reddit_collect("Hedgehog", "hedgehog_request", "./instant-serotonin/data/hedgehdata.p")
