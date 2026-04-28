import sqlite3
import os
from app.backend.table_object_classes.user import User

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DB:
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
                    connection.executescript(sqlfile)

    def get_printable_table(self, table):
        with self.connection as connection:
            cursor = connection.cursor()
            result = cursor.execute(f"SELECT * FROM {table};")

        return result.fetchall()

    def execute_command(self, command, params):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(command, params)

        return cursor

    def get_one(self, command, params):
        return self.execute_command(command, params).fetchone()

    def get_all(self, command, params):
        return self.execute_command(command, params).fetchall()

    def add_feedback(self, form_type, form_content):
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)", (form_type, form_content))
    
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
        

    def get_printers(self):
        query = """
        SELECT
            printer_id,
            printer_name,
            printer_location,
            printer_model,
            curr_status,
            toner_level,
            paper_level,
            last_maintenance
        FROM Printer
        ORDER BY printer_name ASC
        """
        return self.execute_command(query, ())
    

    def get_printer_usage(self):
        query = """
        SELECT
            pu.usage_id,
            p.printer_name,
            p.printer_location,
            pu.pages_printed,
            pu.job_status,
            pu.print_time
        FROM PrinterUsage pu
        JOIN Printer p ON pu.printer_id = p.printer_id
        ORDER BY pu.print_time DESC
        """
        return self.execute_command(query, ())     
    

    def get_printer_usage_summary(self):
        query = """
        SELECT
            p.printer_name,
            COUNT(pu.usage_id) AS total_jobs,
            COALESCE(SUM(pu.pages_printed), 0) AS total_pages
        FROM Printer p
        LEFT JOIN PrinterUsage pu ON p.printer_id = pu.printer_id
        GROUP BY p.printer_id, p.printer_name
        ORDER BY total_pages DESC
        """
        return self.execute_command(query, ()) 

    def get_pending_reservations_count(self):
        query = """
        SELECT COUNT(*)
        FROM RoomReservations
        WHERE status = 'Pending'
        """
        result = self.execute_command(query, ())
        return result[0][0] if result else 0

    def get_printers_needing_attention_count(self):
        query = """
        SELECT COUNT(*)
        FROM Printer
        WHERE toner_level <= 20
        OR paper_level <= 20
        OR curr_status IN ('Offline', 'Maintenance')
        """
        result = self.execute_command(query, ())
        return result[0][0] if result else 0

    def get_library_entry_log(self):
        query = """
        SELECT
            entry_id,
            entry_time,
            entry_count
        FROM LibraryEntryLog
        ORDER BY entry_time ASC
        """
        return self.execute_command(query, ())

    def get_total_entries_today(self):
        query = """
        SELECT COALESCE(SUM(entry_count), 0)
        FROM LibraryEntryLog
        WHERE DATE(entry_time) = DATE('now')
        """
        result = self.execute_command(query, ())
        return result[0][0] if result else 0

    def get_peak_hour_today(self):
        query = """
        SELECT entry_time, entry_count
        FROM LibraryEntryLog
        WHERE DATE(entry_time) = DATE('now')
        ORDER BY entry_count DESC
        LIMIT 1
        """
        result = self.execute_command(query, ())
        return result[0] if result else None



class DBUserFunctions:
    def __init__(self, db:DB):
        self.DB = db

    def add_user(self, user: User):
        command = "INSERT INTO Users (user_name, user_email, user_role) VALUES (?, ?, ?)"
        params = (user.Username, user.Email, user.Role)
        self.DB.execute_command(command, params)

    def get_user(self, email) -> User:
        command = "SELECT * FROM Users WHERE user_email = ?"
        params = (email,)
        result = self.DB.get_one(command, params)

        if result:
            return User(id=result[0], username=result[1], email=result[2], role=result[3])
        else:
            return None

    def remove_user(self, user:User):
        command = "DELETE FROM Users WHERE user_id = ?"
        params = (user.ID,)
        self.DB.execute_command(command, params)

    def edit_user(self, user:User):
        updates = []
        params = []

        if user.Username is not None:
            updates.append("user_name = ?")
            params.append(user.Username)
        if user.Email is not None:
            updates.append("user_email = ?")
            params.append(user.Email)
        if user.Role is not None:
            updates.append("user_role = ?")
            params.append(user.Role)

        if not updates:
            return

        params.append(user.ID)
        command = f"UPDATE Users SET {', '.join(updates)} WHERE user_id = ?"
        self.DB.execute_command(command, params)