from typing import Optional

import requests
from requests import RequestException

from main.config import Config

url = (
    f"https://api.unsplash.com/photos/random"
    f"?client_id={Config.UNSPLASH_API_KEY}&orientation=landscape"
)


def fetch_random_photo() -> Optional[dict]:
    try:
        photo_info = requests.get(url).json()
        return photo_info
    except RequestException:
        return None
