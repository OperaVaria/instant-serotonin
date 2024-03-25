"""
post_class.py

Post dataclass.

Part of the "Instant Serotonin" project by OperaVaria.
"""

# Import dataclass function:
from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    """Class to store data for a singe image post in a standardized way."""
    title: str = "No title"
    source: str
    author: str
    src_url: str
    auth_url: str
    post_url: str
    img_url: str


# Print on accidental run:
if __name__ == '__main__':
    print("Importable module. Not meant to be run!")
