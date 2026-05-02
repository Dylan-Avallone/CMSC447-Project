from app.components.navbar import render_navbar
import streamlit as st
import sys
import os

st.set_page_config(page_title="Feedback Form", page_icon="f", layout="wide")
render_navbar() 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.backend.get_db import get_db

db = get_db()

#home button
if st.button("Back to Home"):
    st.switch_page("pages/home_page.py")

#title
st.title("Feedback")
st.caption("Having issues; recommendations?")


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