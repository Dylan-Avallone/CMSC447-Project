import requests
import streamlit as st
from datetime import datetime, timedelta
from app.backend.get_db import get_db

class RoomAvailabilityScraper:

    def __init__(self):
        self.url = "https://umbc.libcal.com/spaces/availability/grid"
        self.headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://umbc.libcal.com",
            "referer": "https://umbc.libcal.com/spaces?lid=662",
            "user-agent": "Mozilla/5.0",
            "x-requested-with": "XMLHttpRequest"
        }
        self.data = {
            "lid": 662,
            "gid": 0,
            "eid": -1,
            "seat": 0,
            "seatId": 0,
            "zone": 0,
            "start": "",
            "end": "",
            "pageIndex": 0,
            "pageSize": 18
        }
        self.itemIdtoRoomMap = {
            134147: '205',
            134146: '204',
            7820: '457',
            7819: '456',
            7818: '454',
            7817: '453',
            4484: '374',
            4485: '373',
            4486: '372',
            4487: '371',
            4488: '370',
            4489: '369',
            7816: '213',
            7815: '212',
            7814: '211',
            7813: '210',
            30943: '206',
            23252: '207',
            19760: '208',
            19773: '209',
            19774: '231',
            19782: '232'
        }

    def scrape_room_availability(self):
        self.data["start"] = datetime.now().strftime("%Y-%m-%d")
        self.data["end"] = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        res = requests.post(self.url, headers=self.headers, data=self.data)

        return res.json()["slots"]

    # Filters availability data to only those bookings that overlap with the current time. Future bookings can fluctuate, so this should give the most accurate picture of room usage
    def get_current_bookings(self, availability_data):
        current_bookings = []
        current_time = datetime.now()
        for slot in availability_data:
            if 'className' in slot and slot["itemId"] in self.itemIdtoRoomMap:
                if slot["className"] == "s-lc-eq-checkout":
                    startTime = datetime.fromisoformat(slot["start"])
                    endTime = datetime.fromisoformat(slot["end"])
                    if startTime < current_time < endTime:
                        current_bookings.append(slot)

        return current_bookings

    def send_to_db(self, availability_data):
        db = get_db()
        for slot in availability_data:
            if 'className' in slot and slot["itemId"] in self.itemIdtoRoomMap:
                if slot["className"] == "s-lc-eq-checkout":
                    reservation_date = slot["start"][0:10]
                    start_time = slot["start"][11:]
                    end_time = slot["end"][11:]
                    room_id = self.itemIdtoRoomMap[slot["itemId"]]
                    db.add_room_reservation(reservation_date, start_time, end_time, room_id)

@st.cache_data(ttl=3600)
def scrape_hourly():
    print("Scraping Room Availability")
    ra_scraper = RoomAvailabilityScraper()
    availability_data = ra_scraper.scrape_room_availability()
    current_bookings = ra_scraper.get_current_bookings(availability_data)
    ra_scraper.send_to_db(current_bookings)