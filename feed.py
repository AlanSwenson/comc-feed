import feedparser
from bs4 import BeautifulSoup


def get_feed(sport_id="0", search="juan+soto", page_size="100"):
    feed = feedparser.parse(
        f"https://www.comc.com/SearchFeed?SportID={sport_id}&Search={search}&PageSize={page_size}&Sort%3dr"
    )
    return feed


def find_info(entry):
    soup = BeautifulSoup(entry.description, "html.parser")
    secondtd = soup.findAll("td")[1]
    newDict = {}
    for string in secondtd.strings:
        a, *b = string.split(":")
        try:
            newDict[a] = b[0].strip()
        except:
            newDict["title"] = a
        # print(f"{a} {b}")
    print(newDict["title"])
    print(newDict["Qty"])
    print(newDict["Sale Price"])


feed = get_feed()
for entry in feed.entries:
    find_info(entry)

