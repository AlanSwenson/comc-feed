import os

import pytest
import feedparser

from feed import find_info

my_path = os.path.abspath(os.path.dirname(__file__))
feed1 = feedparser.parse(os.path.join(my_path, "support/feed1.rss"))


def test_find_info():
    info = find_info(feed1.entries[0])
    assert (
        info["title"]
        == "2018 Topps Update Series - [Base] #US300.1 - Juan Soto (Vertical, Blue Jersey)"
    )
    assert info["Qty"] == "42"
    assert info["Sale Price"] == "$44.23"

