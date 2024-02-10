"""
reddit_scrape.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Imports:
import praw
import pickle


def reddit_collect(sub_red_name, user_agent_name, file_name):
    """Reddit scraper function.
       Gets all pictures and gifs from hot top 30 of any subreddit.
       Pickles list into a binary file for quick reading.
       Prints number of items collected.
       PRAW and personal reddit app used."""
    
    # Login details.
    reddit = praw.Reddit(
        client_id = "YkfbqV1Dplt5rmDx4hMhDg",
        client_secret = "svXITZ_fW_TzrZzJnd7phvXwqDMoZg",
        user_agent = user_agent_name)
    
    # Set subreddit(s).
    subreddit = reddit.subreddit(sub_red_name)

    # Scrape pictures, create submission list.
    reddit_sub_list = [submission for submission in subreddit.hot(limit=30)
                       if submission.url.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]
    
    # Dump set to picke file.
    with open(file_name, "wb") as file:
        pickle.dump(reddit_sub_list, file)
    
    # Print number of submissions in set.
    print("Number of submissions: " + str(len(reddit_sub_list)))

    return


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module!")
