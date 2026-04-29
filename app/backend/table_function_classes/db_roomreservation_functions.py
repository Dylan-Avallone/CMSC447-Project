from app.backend.db import DB

class DBRRFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def get_room_reservations(self):
        query = """
        SELECT
            rr.reservation_id,
            r.room_name,
            r.room_location,
            r.capacity,
            u.user_name,
            rr.purpose,
            rr.reservation_date,
            rr.start_time,
            rr.end_time,
            rr.status,
            rr.notes,
            rr.created_at
        FROM RoomReservations rr
        JOIN Room r ON rr.room_id = r.room_id
        JOIN Users u ON rr.user_id = u.user_id
        ORDER BY rr.reservation_date ASC, rr.start_time ASC
        """
        params = ()
        return self.db.execute_command(query, params)

    def get_pending_reservations_count(self):
        query = """
        SELECT COUNT(*)
        FROM RoomReservations
        WHERE status = 'Pending'
        """
        params = ()
        result = self.db.execute_command(query, params)
        return result[0][0] if result else 0