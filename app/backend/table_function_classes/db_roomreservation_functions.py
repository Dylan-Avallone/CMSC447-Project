from app.backend.db import DB
from app.backend.constants import NOT_FETCHED
from app.backend.table_object_classes.room_reservation import RoomReservation

class DBRRFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def get_reservations_count(self):
        """
        Returns the number of non-canceled reservations in the DB.
        """
        query = """
        SELECT COUNT(*)
        FROM RoomReservations
        WHERE is_canceled = 0
        """
        params = ()
        result = self.db.get_one(query, params)
        return result[0] if result else 0

    def add_reservations(self, reservations):
        """
        If the combination of the date, start time, and room are unknown to the DB, then just add it. Otherwise, check that the new data is fresher, and if it is, use that.
        Additionally, remove reservations from the DB if the fresher data shows that the reservation has been canceled.
        """
        db_reservations_set = set(self.get_reservations())
        web_reservations_set = set(reservations)
        reservations_to_delete = db_reservations_set - web_reservations_set
        reservations_to_add = web_reservations_set - db_reservations_set
        query = None
        params = None

        for reservation in reservations_to_delete:
            query = "UPDATE RoomReservations SET is_canceled = 1 WHERE room_id = ? AND reservation_date = ? AND start_time = ?"
            params = (reservation.room_id, reservation.date, reservation.start_time)
            self.db.execute_command(query, params)

        for reservation in reservations_to_add:
            if reservation.id != -1: # Already has an assigned ID
                query = "SELECT * FROM RoomReservations WHERE reservation_id = ?"
                params = (reservation.id,)
            else:
                query = "SELECT * FROM RoomReservations WHERE room_id = ? AND reservation_date = ?, AND start_time = ?"
                params = (reservation.id, reservation.date, reservation.start_time)

            result = self.db.get_one(query, params)
            if result:
                if result[5] < reservation.request_timestamp:
                    query = "UPDATE RoomReservations SET created_at = ?, is_canceled = ?, WHERE room_id = ?"
                    params = (reservation.request_timestamp, 0, reservation.id)
            else:
                query = "INSERT INTO RoomReservations (room_id, reservation_date, start_time, end_time, created_at) VALUES (?, ?, ?, ?, ?)"
                params = (reservation.room_id, reservation.date, reservation.start_time, reservation.end_time, reservation.created_at)

            self.db.execute_command(query, params)

    def get_reservations(self):
        """
        Returns a list of all active reservations as RoomReservation objects.
        """
        reservations = []
        query = "SELECT * FROM RoomReservations WHERE is_canceled = 0"
        params = ()
        result = self.db.get_all(query, params)
        if not result is NOT_FETCHED:
            for reservation_ in result:
                reservations.append(RoomReservation(id=reservation_[0],
                                                    room_id=reservation_[1],
                                                    date=reservation_[2],
                                                    start_time=reservation_[3],
                                                    end_time=reservation_[4],
                                                    request_timestamp=reservation_[5]))

        return reservations