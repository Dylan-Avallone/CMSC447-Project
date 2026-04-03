import sqlite3
import os
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DB:
    feedback_limit = 1000
    def __init__(self, name, initializer_files):
        self.filename = name
        self.load_db(self.filename, initializer_files)
        self.tables = [table[0] for table in self.get_tables()]

    def load_db(self, dbname, sqlfiles):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            for file in sqlfiles:
                f = open(os.path.join(BASE_DIR, file), 'r')
                sqlfile = f.read()
                f.close()
                with open(os.path.join(BASE_DIR, file), 'r') as f:
                    sqlfile = f.read()

                sqlCommands = sqlfile.split(';')
                for command in sqlCommands:
                    cursor.execute(command)

    def get_tables(self):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        return cursor.fetchall()

    def add_feedback(self, form_type, form_content):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)", (form_type, form_content))

    def add_user(self, username, email, password):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            hashedpassword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            cursor.execute("INSERT INTO Users (user_name, user_email, user_password) VALUES (?, ?, ?)", (username, email, hashedpassword))
            connection.commit()

    def check_credentials(self, email, password):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE user_email = ?", (email,))
            result = cursor.fetchone()
            returnval = None
            if result is None:
                returnval = False
            else:
                returnval = bcrypt.checkpw(password.encode(), result[3])

            return returnval


        return bool(returnval)

    def get_printable_table(self, table):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            result = cursor.execute(f"SELECT * FROM {table};")

        return result.fetchall()

    def execute_command(self, command, params):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            cursor.execute(command, params)
            result = cursor.fetchall()

        return result

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
        return self.execute_command(query, ())


    def get_rooms(self):
        query = """
        SELECT room_id, room_name, room_location, capacity, room_type
        FROM Room
        ORDER BY room_name ASC
        """
        return self.execute_command(query, ())

