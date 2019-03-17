# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep

all_quotes = []
base_url = "http://quotes.toscrape.com/"
path = "/page/1"


while path:
    res = requests.get(f"{base_url}{path}")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")

    print(f"Scraping {base_url}{path}...")

    for quote in quotes:
        text = quote.find(class_="text").get_text()
        author = quote.find(class_="author").get_text()
        bio_url = quote.find("a")["href"]

        all_quotes.append({
            "text": text,
            "author": author,
            "bio_url": bio_url
        })

    next_btn = soup.find(class_="next") # find next btn with next page url
    path = next_btn.find("a")["href"] if next_btn else None
    sleep(2) # make a pause after each request to not overload server

print(all_quotes)

