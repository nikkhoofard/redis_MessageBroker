import requests
from bs4 import BeautifulSoup
from redis import Redis

client = Redis()


def get_links(url="https://varzesh3.com"):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all('a')
    for link in links:
        value_redis = link.get('href')
        client.rpush('linkss', value_redis)


if __name__ == "__main__":
    get_links()
