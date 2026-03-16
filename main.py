import sqlite3
import streamlit as st
import numpy as np
import pandas as pd

def load_db(dbname: str, sqlfiles) -> None:
    with sqlite3.connect(dbname) as connection:
        cursor = connection.cursor()
        for file in sqlfiles:
            f = open(file)
            sql = f.read()
            f.close()
            commands = sql.split(';')
            for command in commands:
                cursor.execute(command)

def print_table(dbname: str, table: str) -> None:
    with sqlite3.connect(dbname) as connection:
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM Users;")
        rows = result.fetchall()
        for row in rows:
            for value in row:
                print(value)
                st.write(str(value))

load_db('test.db', ['dropDashboardTables.sql',
                                   'createDashboardTables.sql',
                                   'loadStaticDashboardTables.sql'])

print_table('test.db', 'Users')