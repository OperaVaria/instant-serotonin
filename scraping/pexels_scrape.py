"""
pexels_scrape.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Imports:
import requests
from scraping.post_class import Post

def pexels_collect(query, keys):
    """Pexels scraper function.
       Collects top 20 image results.
       Uses direct API request with key."""
    # API request.
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": keys["pexels"]["api_key"]}
    params = {"query": query, "per_page": 20}
    res = requests.get(url = url, headers = headers, params = params, timeout = 60)
    # Error handling.
    if res.ok is not True:
        return res.raise_for_status()
    res_json_data = res.json()
    # Declare post list.
    pexels_list = []
    # Scrape response, create Post objects, append to list.
    for photo in res_json_data["photos"]:
        photo = Post(photo["alt"], "Pexels", photo["photographer"],
                     "https://www.pexels.com/", photo["photographer_url"],
                     photo["url"], photo["src"]["large2x"])
        pexels_list.append(photo)
    # Return list.
    return pexels_list


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module. Not meant to be run!")
