import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DB:
    feedback_limit = 1000
    def __init__(self):
        self.filename = "library_data.db"
        self.load_db(self.filename, ['createDashboardTables.sql'])

    def load_db(self, dbname, sqlfiles):
        connection = sqlite3.connect(dbname)
        cursor = connection.cursor()
        for file in sqlfiles:
            f = open(os.path.join(BASE_DIR, file), 'r')
            sqlfile = f.read()
            f.close()

            sqlCommands = sqlfile.split(';')
            for command in sqlCommands:
                cursor.execute(command)

        connection.commit()
        connection.close()

    def add_feedback(self, form_type, form_content):
        connection = sqlite3.connect(self.filename)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO FeedbackForms (form_type, form_content) VALUES (?, ?)", (form_type, form_content))
        connection.commit()
        connection.close()

    def get_printable_table(self, table):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            result = cursor.execute(f"SELECT * FROM {table};")

        return result.fetchall()