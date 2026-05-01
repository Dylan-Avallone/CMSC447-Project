import sqlite3
import os
from app.backend.constants import NOT_FETCHED

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DB:
    def __init__(self):
        self.file_name = os.path.join(BASE_DIR, "library_data.db")
        self.connection = sqlite3.connect(self.file_name, check_same_thread=False)
        self.load_db(['sql_files/dropDashboardTables.sql',
                      'sql_files/createDashboardTables.sql',
                      'sql_files/loadStaticDashboardTables.sql'])

    def load_db(self, sql_files):
        with self.connection as connection:
            for file in sql_files:
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
        """
        sqlite3's fetchone wrapped with some code. fetchone will return a tuple if a match is found, otherwise None. If fetchone fails,
        this function will return an empty object.
        """
        result = NOT_FETCHED
        try:
            result = self.execute_command(command, params).fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

        return result

    #
    def get_all(self, command, params):
        """
        sqlite3's fetchall wrapped with some code. fetchall will return a list of tuple(s) if match(es) are found, otherwise an empty list. If fetchall fails,
        this function will return an empty object.
        """
        result = NOT_FETCHED
        try:
            result = self.execute_command(command, params).fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

        return result