"""
unsplash_scrape.py

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Imports:
import requests
from scraping.post_class import Post

def unsplash_collect(query, keys):
    """Unsplash scraper function.
       Collects top 20 image results.
       Uses direct API request."""
    # API request.
    url = "https://api.unsplash.com/search/photos"
    headers = {"Accept-Version": "v1"}
    params = {
        "client_id": keys["unsplash"]["access_key"],
        "query": query,
        "per_page": 20,
        "content_filter": "high",
    }
    res = requests.get(url=url, headers=headers, params=params, timeout=60)
    # Error handling.
    if res.ok is not True:
        return res.raise_for_status()
    res_json_data = res.json()
    # Declare post list.
    unsplash_list = []
    # Scrape response, create Post objects, append to list.
    for result in res_json_data["results"]:
        result = Post(
            result["description"],
            "Unsplash",
            result["user"]["name"],
            "https://unsplash.com/",
            result["user"]["links"]["html"],
            result["links"]["html"],
            result["urls"]["regular"],
        )
        unsplash_list.append(result)
    # Return list.
    return unsplash_list


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module. Not meant to be run!")
