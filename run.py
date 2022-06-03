from datetime import timedelta

from main import change_desktop_background_daily
from main.libs.redis_queue import q

if __name__ == "__main__":
    q.enqueue_in(timedelta(seconds=5), change_desktop_background_daily)
