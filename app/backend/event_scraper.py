import requests
from bs4 import BeautifulSoup

class EventScraper:
    def scrape_upcoming_events(self):
        url = "https://my3.my.umbc.edu/groups/library/events"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup("div", class_="event-item content-item")
        for event in soup.find_all("event"):
            print(event)