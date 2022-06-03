import os

from .config import Config
from .engines.desktop import MacDesktop, change_desktop_wallpaper
from .engines.image_processor import save_image_from_url
from .engines.unsplash import fetch_random_photo

os.chdir(os.path.dirname(__file__))


def start_change_desktop_wallpaper():
    photo_info = fetch_random_photo()

    if photo_info:
        save_image_from_url(
            saving_filename=Config.SAVING_IMAGE_FILENAME,
            url=photo_info["links"]["download"],
        )

        change_desktop_wallpaper(
            image_path=os.path.join(os.getcwd(), Config.SAVING_IMAGE_FILENAME)
        )
