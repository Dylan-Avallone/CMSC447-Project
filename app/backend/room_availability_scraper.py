import requests
import warnings
from datetime import datetime, timedelta, time
from app.backend.get_db import get_db
from app.backend.table_function_classes.db_room_functions import DBRoomFunctions
from app.backend.table_function_classes.db_user_functions import DBUserFunctions
from app.backend.table_object_classes.room_reservation import RoomReservation

class RoomAvailabilityScraper:
    URL = "https://umbc.libcal.com/spaces/bookings/search"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "referer": "https://umbc.libcal.com/spaces/bookings?lid=662&gid=0",
        "X-Requested-With": "XMLHttpRequest",
    }
    PARAMS = {
        "lid": 662,
        "gid": 0,
        "draw": 1,
        "start": 0,
        "length": 100,
        "d": "90",  # "Next 90 days" is usually more reliable than "all"
        "customDate": "",
        "search[value]": "",  # The API expects the search object keys
        "search[regex]": "false"
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
    def scrape_room_bookings(self):
        """
        :return: A list of dictionaries returned by the API call representing bookings. An example returned dictionary looks like:
        {'from': '2026-05-11 14:00:00',
        'to': '2026-05-11 15:00:00',
        'nickname': '',
        'itemId': 134146,
        'itemName': '204',
        'itemHasMoreInfo': False,
        'categoryName': 'Individual Study Rooms',
        'categoryUrl': '/spaces?lid=662&gid=7691',
        'locationName': 'AOK Library',
        'seatName': ''}
        """
        res = requests.get(self.URL, headers=self.HEADERS, params=self.PARAMS)
        return res.json()["data"]

    def format_booking_data(self, booking_data):
        """
        Note, all dictionaries without the "className" key (which is how the UMBC library tags timeslots that are reserved) are tossed.
        :param booking_data: A list of dictionaries representing bookings. Probably taken from get_current_bookings().
        :return: A list of RoomReservation objects.
        """
        room_db = DBRoomFunctions(get_db())
        bookings = []
        for reservation in booking_data:
            student_name = reservation["nickname"]
            room_id = room_db.get_room_by_room_number(reservation["itemName"]).id
            date = datetime.fromisoformat(reservation["from"]).date()
            start_time = datetime.fromisoformat(reservation["from"]).time()
            end_time = datetime.fromisoformat(reservation["to"]).time()
            request_timestamp = datetime.now()
            reservation = RoomReservation(-1, student_name, room_id, date, start_time, end_time, request_timestamp)
            bookings.append(reservation)

        return bookings

ra_scraper = RoomAvailabilityScraper()
print(ra_scraper.scrape_room_bookings())
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