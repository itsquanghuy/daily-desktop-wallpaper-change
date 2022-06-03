import os

from .config import Config
from .engines.desktop import MacDesktop, change_desktop_background_image
from .engines.image_processor import save_image_from_url
from .engines.unsplash import fetch_random_photo

os.chdir(os.path.dirname(__file__))


def change_desktop_background_daily():
    photo_info = fetch_random_photo()

    if photo_info:
        save_image_from_url(
            saving_filename=Config.SAVING_IMAGE_FILENAME,
            url=photo_info["links"]["download"],
        )

        change_desktop_background_image(
            image_path=os.path.join(os.getcwd(), Config.SAVING_IMAGE_FILENAME)
        )
