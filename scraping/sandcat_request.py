# Import scraping function:
from reddit_scrape import reddit_collect

# Scrape sand cat subreddit:
reddit_collect("sandcats", "sand_cat_request", "./instant-serotonin/data/scdata.p")
