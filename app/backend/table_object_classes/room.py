from dataclasses import dataclass
from .table_object import TableObject
import datetime

@dataclass
class Room(TableObject):
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

    @classmethod
    def from_row(cls, row):
        try:
            return cls(row["id"],
                row["name"],
                row["location"],
                row["capacity"],
                row["description"],
                row["wd_avblty_start"],
                row["wd_avblty_end"],
                row["sat_avblty_start"],
                row["sat_avblty_end"],
                row["sun_avblty_start"],
                row["sun_avblty_end"])
        except (KeyError, IndexError) as e:
            raise AttributeError(f"Database Mapping Error: Column {e} not found in row passed to from_row") from e