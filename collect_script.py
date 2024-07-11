"""
collect_script.py

Scheduled script to collect data for webapp.

Part of the "Instant Serotonin" project by OperaVaria.
"""

# External imports:
import pickle
from pathlib import Path
from yaml import safe_load

# Import scraping functions:
from scraping.pexels_scrape import pexels_collect
from scraping.pixabay_scrape import pixabay_collect
from scraping.reddit_scrape import reddit_collect
from scraping.unsplash_scrape import unsplash_collect


def scrape(animal_name, query, subreddits, keys):
    """Call collecting functions and assemble pickle file form retuned lists."""
    # Reddit
    reddit_list = reddit_collect(subreddits, keys)
    # Pexels
    pexels_list = pexels_collect(query, keys)
    # Pixabay
    pixabay_list = pixabay_collect(query, keys)
    # Unsplash
    unsplash_list = unsplash_collect(query, keys)
    # Join lists.
    # Sand cat and manul results are problematic, therefore skip sites.
    if animal_name == "sand_cat":
        post_list = reddit_list
    elif animal_name == "manul":
        post_list = reddit_list + pixabay_list + unsplash_list
    else:
        post_list = reddit_list + pexels_list + pixabay_list + unsplash_list
    # Pickle data.
    pfile_path = (Path(__file__).parents[0].resolve()).joinpath(f"data/{animal_name}_data.p")
    with open(pfile_path, "wb") as file:
        pickle.dump(post_list, file)
    # Print number of items.
    return print(f"Number of {animal_name} posts: {str(len(post_list))}")


def main():
    """Image scraping main function."""
    # Load login information file.
    keys_path = (Path(__file__).parents[0].resolve()).joinpath("scraping/auth/keys.yaml")
    with open(keys_path, "r", encoding="utf-8") as keys_file:
        keys = safe_load(keys_file)
    # Collect capybara content.
    scrape("capybara", "capybara", "capybara+capybaras+capybarasoncritters", keys)
    # Collect hedgehog content.
    scrape("hedgehog", "hedgehog", "Hedgehog+Hedgehogs+HedgehogsAreLiquid", keys)
    # Collect manul content.
    scrape("manul", "manul", "PallasCats+manuls", keys)
    # Collect sand cat content.
    scrape("sand_cat","'sand cat'", "sandcats", keys)
    # Print final message.
    return print("Scraping completed.")


# Run main function.
if __name__ == '__main__':
    main()
