import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.backend.get_db import get_db

db = get_db("library_data")

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns([1,4,1])

with col1:
    st.button("Back")

with col2:
    st.space("medium")
    option = st.selectbox(
        "Select an option",
        ["Bug Report",
                "Feature Request",
                "Compliment"]
    )
    max_chars = 1000
    content = st.text_area("Enter your feedback", max_chars=max_chars)
    container = st.container(horizontal_alignment="center")
    submit = container.button("Submit")

if submit:
    db.add_feedback(option, content)
    st.write(db.get_printable_table("FeedbackForms"))
    st.write(db.tables)