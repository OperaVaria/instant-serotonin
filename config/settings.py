""" Flask and Flask extensions configuration file. """

# Imports:
from datetime import timedelta
from pathlib import Path
from cachelib.file import FileSystemCache

# Minify settings:
bypass = ["robots_txt", "humans_txt", "sitemap_xml"]

# Session settings:
SESSIONS_PATH = (Path(__file__).parents[1].resolve()).joinpath("flask_session/")
SESSION_TYPE = "cachelib"
SESSION_CACHELIB = FileSystemCache(threshold=500, cache_dir=SESSIONS_PATH)
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Strict"

# Talisman settings:
csp = {
    "default-src": ["'none'"],
    "connect-src": ["'self'"],
    "script-src": [
        "'self'",
        "'sha256-/Nhp/0Mc72DYgT/sMpiOn5EDx8z4guopcViJmqvMUy0='",
    ],
    "style-src": ["'self'"],
    "img-src": ["*"],
    "font-src": ["'self'"],
    "object-src": ["'none'"],
    "base-uri": ["'none'"],
    "form-action": ["'self'"],
}

# Display message when accidentally run:
if __name__ == "__main__":
    print("This is a config file. Not meant to be run!")
