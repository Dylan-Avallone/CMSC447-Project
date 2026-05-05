from dataclasses import dataclass
from typing import ClassVar
from .table_object import TableObject
import datetime

@dataclass
class Room(TableObject):
    id: int
    type: str
    number: str
    capacity: int
    description: str
    wd_availability_start: datetime.time
    wd_availability_end: datetime.time
    sat_availability_start: datetime.time
    sat_availability_end: datetime.time
    sun_availability_start: datetime.time
    sun_availability_end: datetime.time
    TYPES: ClassVar[list] = ['Group', 'Individual']

    def __post_init__(self):
        if self.capacity <= 0:
            raise AttributeError("Room capacity must be greater than 0")
        if self.wd_availability_start > self.wd_availability_end:
            raise AttributeError("Room wd_availability_start must be before wd_availability_end")
        if self.sat_availability_start > self.sat_availability_end:
            raise AttributeError("Room sat_availability_start must be before sat_availability_end")
        if self.sun_availability_start > self.sun_availability_end:
            raise AttributeError("Room sun_availability_start must be before sun_availability_end")
        if self.type not in self.TYPES:
            raise ValueError("Invalid type {}".format(self.type))

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

    def to_row(self):
        return {"id": self.id,
                "name": self.name,
                "location": self.location,
                "capacity": self.capacity,
                "description": self.description,
                "wd_avblty_start": self.wd_availability_start,
                "wd_avblty_end": self.wd_availability_end,
                "sat_avblty_start": self.sat_availability_start,
                "sat_avblty_end": self.sat_availability_end,
                "sun_avblty_start": self.sun_availability_start,
                "sun_avblty_end": self.sun_availability_end}