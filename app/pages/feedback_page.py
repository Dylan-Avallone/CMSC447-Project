import streamlit as st
import sys
import os
import smtplib
from email.message import EmailMessage

from app.backend.table_object_classes.feedback import Feedback
from app.backend.table_function_classes.db_feedback_functions import DBFeedbackFunctions
from app.backend.get_db import get_db

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

def notify_developers(feedback_content, developer_emails):
    # Configuration (Use environment variables for security!)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your-system@gmail.com"
    SENDER_PASSWORD = "your-app-password"

    for recipient in developer_emails:
        msg = EmailMessage()
        msg.set_content(f"New Feedback Submitted:\n\n{feedback_content}")
        msg["Subject"] = "Alert: New System Feedback"
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Secure the connection
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print(f"Failed to send to {recipient}: {e}")

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

content = st.text_area("Enter your feedback", max_chars=max_chars)
submit = st.button("Submit")
if submit:
    db.add_feedback(option, content)

    st.write(db.get_printable_table("FeedbackForms"))