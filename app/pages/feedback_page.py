import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.backend.get_db import get_db

db = get_db()

option = st.selectbox(
    "Select an option",
    ["Bug Report",
            "Feature Request",
            "Compliment"]
)

max_chars = 1000
content = st.text_area("Enter your feedback", max_chars=max_chars)
submit = st.button("Submit")
if submit:
    db.add_feedback(option, content)
    st.write(db.get_printable_table("FeedbackForms"))