import feedparser
from bs4 import BeautifulSoup

from models import Card, Record, session


def get_feed(sport_id="0", search="juan+soto", page_size="100"):
    feed = feedparser.parse(
        f"https://www.comc.com/SearchFeed?SportID={sport_id}&Search={search}&PageSize={page_size}&Sort%3dr"
    )
    return feed


def create_card(strings):
    card = {}
    for string in strings:
        a, *b = string.split(":")
        try:
            b = b[0].strip()
            if a == "Sale Price":
                card["price"] = b.replace("$", "")
            elif a == "Qty":
                card["qty"] = b
        except:
            card["title"] = a
    return card


def find_info(entry):
    soup = BeautifulSoup(entry.description, "html.parser")
    secondtd = soup.findAll("td")[1]
    card = create_card(secondtd.strings)
    card_obj = session.query(Card).filter(Card.title == card["title"]).one_or_none()
    if card_obj is None:
        card_obj = Card(title=card["title"])
    record = Record(qty=card["qty"], price=card["price"])
    card_obj.records.append(record)
    print(f"{card_obj}")
    for record in card_obj.records:
        print(f"{record}")

    return card_obj


if __name__ == "__main__":
    feed = get_feed()
    cards = []
    for entry in feed.entries:
        cards.append(find_info(entry))

    session.add_all(cards)
    session.commit()
