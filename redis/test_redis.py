from redis import Redis
import random

client = Redis()


def import_users_data(count):
    for i in range(count):
        client.set(f" key:{i}", random.randint(1, 10))

    print(f"{count} user added to redis")


if __name__ == "__main__":
    import_users_data(10000)
