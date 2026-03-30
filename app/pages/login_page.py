import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.backend.get_db import get_db

db = get_db("library_data")

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([1,4,1])

with col1:
    back = st.button("Back")

with col2:
    st.space("medium")
    email = st.text_input("Email")
    password = st.text_input("Password")
    container = st.container(horizontal_alignment="center")
    submit = container.button("Submit")

if submit:
    db.add_user("Ryan", "ryano3@umbc.edu", "password")
    st.write(db.check_credentials(email.strip(), password.strip()))

if back:
    st.switch_page("main.py")