from rq import Connection, Queue, Worker

from main.libs.redis_queue import connection

if __name__ == "__main__":
    listen = ["default"]
    with Connection(connection):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
