import sqlite3
import streamlit as st
import numpy as np
import pandas as pd



def print_table(dbname: str, table: str) -> None:
    with sqlite3.connect(dbname) as connection:
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM Users;")
        rows = result.fetchall()
        for row in rows:
            for value in row:
                print(value)
                st.write(str(value))

if st.button("Feedback Form"):
    st.switch_page("pages/feedback_form.py")

"""
load_db('test.db', ['dropDashboardTables.sql',
                                   'createDashboardTables.sql',
                                   'loadStaticDashboardTables.sql'])

print_table('test.db', 'Users')
"""