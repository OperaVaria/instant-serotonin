"""
pixabay_scrape.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Imports:
import requests
from scraping.post_class import Post

def pixabay_collect(query, keys):
    """Pixabay scraper function.
       Collects top 20 image results.
       Uses direct API request."""
    # API request.
    url = "https://pixabay.com/api/"
    params = {"key": keys["pixabay"]["api_key"], "q": query,
              "image_type":"photo", "safesearch": "true"}
    res = requests.get(url = url, params = params, timeout = 60)
    # Error handling.
    if res.ok is not True:
        return res.raise_for_status()
    res_json_data = res.json()
    # Declare post list.
    pixab_list = []
    # Scrape response, create Post objects, append to list.
    for hit in res_json_data["hits"]:
        hit = Post(f"Pixabay image (id: {hit['id']})",
                   "Pixabay", hit["user"], "https://pixabay.com/",
                   f"https://pixabay.com/users/{hit['user']}-{hit['user_id']}/",
                   hit["pageURL"], hit["largeImageURL"])
        pixab_list.append(hit)
    # Return list.
    return pixab_list


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module. Not meant to be run!")
