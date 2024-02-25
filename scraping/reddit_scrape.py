"""
reddit_scrape.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# External module imports:
import praw
import pickle

# Login variable imports:
from reddit_login import id, secret


def reddit_collect(sub_red_name, user_agent_name, file_name):
    """Reddit scraper function.
       Gets all pictures and gifs from hot top 30 of any subreddit.
       Pickles list into a binary file for quick reading.
       Prints number of items collected.
       PRAW and personal reddit app used."""    
    # Login details.
    reddit = praw.Reddit(
        client_id = id,
        client_secret = secret,
        user_agent = user_agent_name)    
    # Set subreddit(s).
    subreddit = reddit.subreddit(sub_red_name)
    # Scrape posts, create submission list.
    reddit_sub_list = [submission for submission in subreddit.hot(limit=30)
                       if submission.url.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]    
    # Dump list to picke file.
    with open(file_name, "wb") as file:
        pickle.dump(reddit_sub_list, file)    
    # Print number of submissions in set.
    print("Number of submissions: " + str(len(reddit_sub_list)))
    return


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module. Not meant to be run!")
