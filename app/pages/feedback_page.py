import streamlit as st
import sys
import os
import smtplib
from email.message import EmailMessage
from app.backend.table_object_classes.user import User
from app.backend.table_object_classes.feedback import Feedback
from app.backend.table_function_classes.db_feedback_functions import DBFeedbackFunctions
from app.backend.table_function_classes.db_user_functions import DBUserFunctions
from app.backend.constants import NOT_FETCHED
from app.backend.get_db import get_db
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

db = get_db()
feedback_functions = DBFeedbackFunctions(db)
user_functions = DBUserFunctions(db)

if not "user" in st.session_state:
    if st.user.is_logged_in:
        st.session_state["user"] = user_functions.get_user(st.user.email)
    else:
        st.session_state["user"] = User()

def email_feedback(feedback_:Feedback):
    dev_emails = [user.email for user in user_functions.get_users_by_role("developer")]
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "librarydashboard39@gmail.com"
    sender_password = st.secrets["EMAIL_PASSWORD"]

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            for recipient in dev_emails:
                msg = EmailMessage()
                msg.set_content(f"New {feedback_.type} submitted:\n\n{feedback_.content}")
                msg["Subject"] = "Alert: New System Feedback"
                msg["From"] = sender_email
                msg["To"] = recipient
                server.send_message(msg)
    except Exception as e:
        print(f"SMTP Error: {e}")

#home button
if st.button("Back to Home"):
    st.switch_page("pages/home_page.py")

#title
st.title("Feedback")
st.caption("Having issues; recommendations?")

option = st.selectbox("Select an option", Feedback.TYPES, format_func=lambda o: o.title())
content = st.text_area("Enter your feedback", max_chars=Feedback.MAX_LENGTH)

submit = st.button("Submit")
if submit:
    most_recent_feedback = feedback_functions.get_last_feedback(st.session_state["user"])
    time_since_last_submission = sys.maxsize
    if most_recent_feedback is NOT_FETCHED:
        st.write("Failed to try to fetch user feedback")
    else:
        if most_recent_feedback.created_at is not None:
            time_since_last_submission = datetime.now() - most_recent_feedback.created_at

    if time_since_last_submission.minutes < 5:
        st.error("Can't submit feedback less than 5 minutes apart. Please wait {} minutes before submitting.".format(5 - time_since_last_submission.minutes))
    elif content is None:
        st.error("Please enter a description before submitting!")
    else:
        feedback = Feedback(option, content)
        feedback_functions.add_feedback(feedback)
        email_feedback(feedback)
        st.success("Feedback submitted successfully!")

    st.write(db.get_printable_table("FeedbackForms"))