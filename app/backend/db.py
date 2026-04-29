import sqlite3
import os

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
        return self.execute_command(command, params).fetchone()

    def get_all(self, command, params):
        return self.execute_command(command, params).fetchall()