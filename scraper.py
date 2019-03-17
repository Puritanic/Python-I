# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

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
    sleep(0.5) # make a pause after each request to not overload server

# print(all_quotes)
remaining_guesses = 4
quote = choice(all_quotes)
guess = ""
print(quote["text"])
print(quote["author"])

while guess.strip().lower() != quote["author"].lower():
    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
    remaining_guesses -= 1

    if guess == quote["author"]:
        print("That's right!")
        break

    if remaining_guesses == 3:
        res = requests.get(f"{base_url}{quote['bio_url']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint: The author was born {birth_date} in {birth_place}")
    elif remaining_guesses == 2:
        print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
    elif remaining_guesses == 1 :
        last_initial = quote['author'].split(" ")[1][0]
        print(f"Here's a hint: The author's last name starts with: {last_initial}")
    else:
        print(f"Sorry, you've run out of guesses. The correct answer was {quote['author']}")
        break
