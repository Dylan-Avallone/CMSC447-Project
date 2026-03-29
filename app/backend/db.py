import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class DB:
    feedback_limit = 1000
    def __init__(self):
        self.filename = "library_data.db"
        self.load_db(self.filename, ['dropDashboardTables.sql',
                                     'createDashboardTables.sql',
                                     'loadStaticDashboardTables.sql'])
        self.connection = sqlite3.connect(self.filename)

    def load_db(self, dbname, sqlfiles):
        with self.connection as connection:
            for file in sqlfiles:
                f = open(os.path.join(BASE_DIR, file), 'r')
                sqlfile = f.read()
                f.close()

                sqlCommands = sqlfile.split(';')
                for command in sqlCommands:
                    connection.cursor.execute(command)

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