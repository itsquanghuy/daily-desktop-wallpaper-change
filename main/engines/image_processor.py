import requests


def save_image_from_url(saving_filename: str, url: str) -> None:
    image_stream = requests.get(url, stream=True)
    with open(saving_filename, "wb") as f:
        for chunk in image_stream:
            f.write(chunk)
