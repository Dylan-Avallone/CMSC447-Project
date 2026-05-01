from dataclasses import dataclass
import datetime

@dataclass
class Room:
    id: int
    name: str
    location: str
    capacity: int
    description: str
    wd_availability_start: datetime.time
    wd_availability_end: datetime.time
    sat_availability_start: datetime.time
    sat_availability_end: datetime.time
    sun_availability_start: datetime.time
    sun_availability_end: datetime.time