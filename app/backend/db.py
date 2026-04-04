import sqlite3
import os
from pathlib import Path
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = PROJECT_ROOT = Path(__file__).resolve().parents[2]
class DB:
    feedback_limit = 1000
    def __init__(self, name, initializer_files):
        self.dbname = name
        self.dbpath = os.path.join(PROJECT_ROOT, "app", self.dbname) # Make the path to the DB absolute so there doesn't end up being multiple copies
        self.load_db(self.dbname, initializer_files)
        self.tables = [table[0] for table in self.get_tables()]

    def load_db(self, dbname, sqlfiles):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            for file in sqlfiles:
                with open(os.path.join(BASE_DIR, file), 'r') as f:
                    sqlfile = f.read()

                sqlCommands = sqlfile.split(';')
                for command in sqlCommands:
                    try:
                        cursor.execute(command)
                    except sqlite3.IntegrityError: # Get past the unique constraint by simply not adding the item
                        pass

    def get_tables(self):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        return cursor.fetchall()

    def add_feedback(self, form_type, form_content):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)", (form_type, form_content))

    def add_user(self, username, email, password):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            hashedpassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            cursor.execute("INSERT INTO Users (user_name, user_email, user_password) VALUES (?, ?, ?)", (username, email, hashedpassword))
            connection.commit()

    def add_room_reservation(self, reservation_date, start_time, end_time, room_location):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute("INSERT INTO RoomReservation (reservation_date, start_time, end_time, room_location) VALUES (?, ?, ?, ?)", (reservation_date, start_time, end_time, room_location))
            except sqlite3.IntegrityError: # Also ignore duplicates here, rather than inserting them again
                pass

    def check_credentials(self, email, password):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE user_email = ?", (email,))
            result = cursor.fetchone()
            returnval = None
            if result is None:
                returnval = False
            else:
                returnval = bcrypt.checkpw(password.encode(), result[3])

        return bool(returnval)

    def get_printable_table(self, table):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            result = cursor.execute(f"SELECT * FROM {table};")

        return result.fetchall()

    def execute_command(self, command, params):
        with sqlite3.connect(self.dbpath) as connection:
            cursor = connection.cursor()
            cursor.execute(command, params)
            result = cursor.fetchall()

        return result

    def get_room_reservations(self):
        query = """
        SELECT
            rr.reservation_id,
            rr.purpose,
            rr.reservation_date,
            rr.start_time,
            rr.end_time,
            rr.notes,
            rr.created_at,
            u.user_name,
            r.room_location
        FROM RoomReservation rr
        LEFT JOIN Users u ON rr.user_id = u.user_id
        LEFT JOIN Room r ON rr.room_location = r.room_location
        ORDER BY rr.reservation_date ASC, rr.start_time ASC
        """
        return self.execute_command(query, ())


    def get_rooms(self):
        query = """
        SELECT room_id, room_name, room_location, capacity, room_type
        FROM Room
        ORDER BY room_name ASC
        """
        return self.execute_command(query, ())

