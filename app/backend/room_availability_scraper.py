import requests
import warnings
from datetime import datetime, timedelta, time
from app.backend.get_db import get_db
from app.backend.table_function_classes.db_room_functions import DBRoomFunctions
from app.backend.table_object_classes.room_reservation import RoomReservation

class RoomAvailabilityScraper:
    URL = "https://umbc.libcal.com/spaces/availability/grid"
    HEADERS = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://umbc.libcal.com",
        "referer": "https://umbc.libcal.com/spaces?lid=662",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }
    DATA = {
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

    # There's a few IDs here that don't map to any visible rooms on the page. For completeness I still included them and marked them as None type.
    ITEM_ID_TO_ROOM_MAP = {
        4482: 'RLC Seminar Room',
        4484: '374',
        4485: '373',
        4486: '372',
        4487: '371',
        4488: '370',
        4489: '369',
        7813: '210',
        7814: '211',
        7815: '212',
        7816: '213',
        7817: '453',
        7818: '454',
        7819: '456',
        7820: '457',
        7821: '755',
        14465: '258',
        19760: '208',
        19773: '209',
        19774: '231',
        19782: '232',
        23252: '207',
        30943: '206',
        30977: '257',
        43107: '368',
        107579: None,
        107867: None,
        113401: None,
        115150: None,
        134141: None,
        134144: None,
        134145: None,
        134146: '204',
        134147: '205',
        144560: None,
        144561: None,
        144562: None,
        144563: None,
        144564: None,
        144565: None,
        144566: None,
        144567: None,
        144568: None
    }
    MAX_REQUESTABLE_DAYS = 31

    # Apparently, requesting more than 31 days of room booking data causes an error.
    # To handle this, then, I will split requests for more than 31 days of data into multiple requests.
    def scrape_room_availability(self, start_day_, end_day_):
        """
        :param start_day_: A datetime.date object.
        :param end_day_: A datetime.date object.
        :return: A list of dictionaries returned by the API call representing timeslots, reserved or not.
        """
        result = []
        start_day = start_day_
        temp_end_day = start_day_
        end_day = end_day_
        num_days = (end_day_ - start_day).days
        while num_days > 0:
            days_requested = min(num_days, self.MAX_REQUESTABLE_DAYS)
            temp_end_day += timedelta(days=days_requested)
            self.DATA["start"] = start_day.strftime("%Y-%m-%d")
            self.DATA["end"] = temp_end_day.strftime("%Y-%m-%d")
            res = requests.post(self.URL, headers=self.HEADERS, data=self.DATA)
            result.extend(res.json()["slots"])
            start_day = end_day
            num_days -= days_requested

        return result

    def format_availability_data(self, availability_data):
        """
        Note, all dictionaries without the "className" key (which is how the UMBC library tags timeslots that are reserved) are tossed.
        :param availability_data: A list of dictionaries representing bookings. Probably taken from get_current_bookings().
        :return: A list of RoomReservation objects.
        """
        room_db = DBRoomFunctions(get_db())
        bookings = []
        for slot in availability_data:
            if 'className' in slot and slot["itemId"] in self.ITEM_ID_TO_ROOM_MAP:
                if self.ITEM_ID_TO_ROOM_MAP[slot["itemId"]] is None:
                    warnings.warn("The system doesn't a name for this room!")
                else:
                    if slot["className"] == "s-lc-eq-checkout":
                        room_id = room_db.get_room_by_location(self.ITEM_ID_TO_ROOM_MAP[slot["itemId"]]).id
                        date = datetime.fromisoformat(slot["start"]).date()
                        start_time = datetime.fromisoformat(slot["start"]).time()
                        end_time = datetime.fromisoformat(slot["end"]).time()
                        request_timestamp = datetime.now()
                        reservation = RoomReservation(-1, room_id, date, start_time, end_time, request_timestamp)
                        bookings.append(reservation)
                    else:
                        warnings.warn("Unknown className encountered. You should check on this.")

        return bookings

    # Filters availability data to only those bookings that overlap with the current time.
    # Future bookings can fluctuate, so this should give the most accurate picture of room usage.
    def get_current_bookings(self, availability_data):
        current_bookings = []
        current_time = datetime.now()
        for slot in availability_data:
            if 'className' in slot and slot["itemId"] in self.ITEM_ID_TO_ROOM_MAP:
                if slot["className"] == "s-lc-eq-checkout":
                    start_time = datetime.fromisoformat(slot["start"])
                    end_time = datetime.fromisoformat(slot["end"])
                    if start_time < current_time < end_time:
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
                    room_location = self.itemIdtoRoomMap[slot["itemId"]]
                    db.add_room_reservation(reservation_date, start_time, end_time, room_location)

"""
#@st.cache_data(ttl=3600)
def scrape_hourly():
    # 5/23/26 is a week out from start of finals, the calendar stops showing slots on this day
    days_until_semester_end = get_days_until_semester_end()
    ra_scraper = RoomAvailabilityScraper()
    availability_data = ra_scraper.scrape_room_availability(10)
    ra_scraper.send_to_db(availability_data)

# Gotta see what the library availability is like for summer and winter semesters
def get_days_until_semester_end():
    return_val = None
    today = date.today()
    curr_year = today.year

    spring_sem_start = date(curr_year, 1, 19)
    spring_sem_end = date(curr_year, 5, 30)

    fall_sem_start = date(curr_year, 8, 25)
    fall_sem_end = date(curr_year, 12, 27)

    if spring_sem_start <= today <= spring_sem_end: # Spring Semester
        return_val = (spring_sem_end - today).days
    elif fall_sem_start <= today <= fall_sem_end: # Fall Semester
        return_val = (fall_sem_end - today).days
    else:
        return_val = 0

    return return_val

ra_scraper = RoomAvailabilityScraper()
availability_data = ra_scraper.scrape_room_availability(3)
current_bookings = ra_scraper.get_current_bookings(availability_data)
print(availability_data)
"""