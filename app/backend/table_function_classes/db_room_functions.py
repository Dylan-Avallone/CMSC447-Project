from app.backend.db import DB
from app.backend.table_object_classes.room import Room

class DBRoomFunctions:
    def __init__(self, db_:DB):
        self.db = db_

    def get_rooms(self):
        query = """
        SELECT room_id, room_name, room_location, capacity, room_type
        FROM Room
        ORDER BY room_name ASC
        """
        params = ()
        return self.db.get_all(query, params)

    def get_room_by_location(self, room_location):
        query = "Select * From Rooms Where room_location = '{}'".format(room_location)
        params = ()
        result = self.db.get_one(query, params)
        return Room(result)