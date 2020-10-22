import os

import pytest
import feedparser

from feed import find_info

my_path = os.path.abspath(os.path.dirname(__file__))
feed1 = feedparser.parse(os.path.join(my_path, "support/feed1.rss"))


def test_find_info():
    card = find_info(feed1.entries[0])
    assert (
        card.title
        == "2018 Topps Update Series - [Base] #US300.1 - Juan Soto (Vertical, Blue Jersey)"
    )
    # assert card.qty == "42"
    # assert card.price == "44.23"
