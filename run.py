from datetime import timedelta

from main import start_change_desktop_wallpaper
from main.libs.redis_queue import q

if __name__ == "__main__":
    q.enqueue_in(timedelta(seconds=5), start_change_desktop_wallpaper)
