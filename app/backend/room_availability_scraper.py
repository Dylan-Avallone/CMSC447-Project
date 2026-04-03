import requests
from datetime import datetime, timedelta

def scrape_room_availability():
    url = "https://umbc.libcal.com/spaces/availability/grid"

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://umbc.libcal.com",
        "referer": "https://umbc.libcal.com/spaces?lid=662",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }

    start = datetime.now().strftime("%Y-%m-%d")
    end = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    print(start)
    print(end)
    data = {
        "lid": 662,
        "gid": 0,
        "eid": -1,
        "seat": 0,
        "seatId": 0,
        "zone": 0,
        "start": start,
        "end": end,
        "pageIndex": 0,
        "pageSize": 18
    }

    res = requests.post(url, headers=headers, data=data)

    print(res.status_code)
    print(res.headers.get("content-type"))

    data = res.json()
    for slot in data["slots"]:
        print(slot)

scrape_room_availability()
'''

'''