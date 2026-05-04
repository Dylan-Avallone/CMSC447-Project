from dataclasses import dataclass
import datetime

@dataclass
class RoomReservation:
    id: int
    room_id: int
    date: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    request_timestamp: datetime.datetime
    is_canceled: int = 0

    def __eq__(self, other):
        """
        Two RoomReservation objects are equal given they share the same room_id, date, and start_time
        """
        if not isinstance(other, RoomReservation):
            is_equal = False
        else:
            is_equal = (self.room_id == other.room_id) and (self.date == other.date) and (self.start_time == other.start_time)

        return is_equal

    def __hash__(self):
        return hash((self.room_id, self.date, self.start_time))

    @classmethod
    def from_row(cls, row):
        try:
            return cls(row["id"],
                       row["room_id"],
                       row["reservation_date"],
                       row["start_time"],
                       row["end_time"],
                       row["request_timestamp"],)
        except (KeyError, IndexError) as e:
            raise AttributeError(f"Database Mapping Error: Column {e} not found in row passed to from_row") from e