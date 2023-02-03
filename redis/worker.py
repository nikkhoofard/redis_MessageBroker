import sys
from redis import Redis

client = Redis()


def watch_links(name):
    print(f"worker {name} started")
    while True:
        link = client.blpop('linkss')
        print(link)

    print(f"worker {name} ended")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise KeyError("worker name is not required")
    watch_links(sys.argv[1])
