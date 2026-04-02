import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DB:
    feedback_limit = 1000
    def __init__(self):
        self.filename = os.path.join(BASE_DIR, "library_data.db")
        self.connection = sqlite3.connect(self.filename, check_same_thread=False)
        self.load_db(self.filename, ['dropDashboardTables.sql',
                                     'createDashboardTables.sql',
                                     'loadStaticDashboardTables.sql'])
     

    def load_db(self, dbname, sqlfiles):
        with self.connection as connection:
            for file in sqlfiles:
                with open(os.path.join(BASE_DIR, file), 'r') as f:
                    sqlfile = f.read()

                sqlCommands = sqlfile.split(';')
                for command in sqlCommands:
                    command = command.strip()
                    if not command:
                        continue
                    connection.cursor().execute(command)

    def add_feedback(self, form_type, form_content):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)", (form_type, form_content))

    def add_user(self, username, email, password):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Users (user_name, user_email, user_password) VALUES (?, ?, ?)", (username, email, password))
            connection.commit()

    def check_credentials(self, email, password):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT EXISTS(SELECT 1 FROM Users WHERE user_email = ? AND user_password = ?)", (email, password))
            returnval = cursor.fetchone()[0]

        return bool(returnval)


    def get_printable_table(self, table):
        with self.connection as connection:
            cursor = connection.cursor()
            result = cursor.execute(f"SELECT * FROM {table};")

        return result.fetchall()

    def execute_command(self, command, params):
        with self.connection as connection:
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
        
