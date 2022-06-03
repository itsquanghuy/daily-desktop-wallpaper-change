import redis
from rq import Queue

from main.config import Config

connection = redis.from_url(Config.REDIS_URL)
q = Queue(connection=connection)
