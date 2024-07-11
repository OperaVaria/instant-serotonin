"""
reddit_scrape.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Imports:
from sys import platform
import praw
from scraping.post_class import Post


def reddit_collect(sub_red_name, keys):
    """Reddit scraper function.
       Gets all pictures and gifs from hot top 30 of any subreddit.
       PRAW and personal reddit app login used."""
    # Login details.
    reddit = praw.Reddit(
        client_id = keys["reddit_app"]["id"],
        client_secret = keys["reddit_app"]["secret"],
        user_agent = f"{platform}:instant-serotonin:v2.0.1 (by u/just_want_api)")
    # Set subreddit(s).
    subreddit = reddit.subreddit(sub_red_name)
    # Declare post list.
    reddit_post_list = []
    # Scrape submissions, create Post objects, append to list.
    for submission in subreddit.hot(limit=30):
        if submission.url.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            post = Post(
                submission.title,
                f"r/{submission.subreddit.display_name}",
                submission.author,
                f"https://www.reddit.com/r/{submission.subreddit.display_name}/",
                f"https://www.reddit.com/user/{submission.author}/",
                f"https://www.reddit.com{submission.permalink}",
                submission.url,
            )
            reddit_post_list.append(post)
    # Return list.
    return reddit_post_list


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module. Not meant to be run!")
