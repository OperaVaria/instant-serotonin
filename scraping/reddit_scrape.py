# Imports:
import praw
import pickle


def reddit_collect(sub_red_name, user_agent_name, file_name):
    """Reddit scraper function. Gets all pictures from hot top 30 of a subreddit.
       Pickles it into a file.
       PRAW and personal reddit app used."""
    
    reddit = praw.Reddit(
        client_id = "YkfbqV1Dplt5rmDx4hMhDg",
        client_secret = "svXITZ_fW_TzrZzJnd7phvXwqDMoZg",
        user_agent = user_agent_name)

    subreddit = reddit.subreddit(sub_red_name)

    global reddit_sub_list
    reddit_sub_list = [submission for submission in subreddit.hot(limit=30)
                       if submission.url.lower().endswith((".png", ".jpg", ".jpeg"))]
    with open(file_name, "wb") as file:
        pickle.dump(reddit_sub_list, file)
    return

# Print on accidental run:
if __name__ == '__main__':
    print("Importable module!")
