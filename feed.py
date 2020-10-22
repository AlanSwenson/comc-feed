import feedparser
from bs4 import BeautifulSoup

from models import Card, session


def get_feed(sport_id="0", search="juan+soto", page_size="100"):
    feed = feedparser.parse(
        f"https://www.comc.com/SearchFeed?SportID={sport_id}&Search={search}&PageSize={page_size}&Sort%3dr"
    )
    return feed


def find_info(entry):
    soup = BeautifulSoup(entry.description, "html.parser")
    secondtd = soup.findAll("td")[1]
    card = Card()
    for string in secondtd.strings:
        a, *b = string.split(":")
        try:
            b = b[0].strip()
            if a == "Sale Price":
                card.price = b.replace("$", "")
            elif a == "Qty":
                card.qty = b
        except:
            card.title = a
    print(f"{card}")

    return card


if __name__ == "__main__":
    feed = get_feed()
    cards = []
    for entry in feed.entries:
        cards.append(find_info(entry))

    session.add_all(cards)
    session.commit()
