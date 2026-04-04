import streamlit as st
from pathlib import Path
from app.backend.room_availability_scraper import *

scrape_hourly()

st.set_page_config(page_title="Library Dashboard", page_icon="X", layout="wide")

#assets access dir (images)
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


left, right = st.columns([12, 1])

with left:
    st.title("UMBC Library Dashboard")
    st.caption("Operations Portal")      

with right:
    st.image(ASSETS_DIR / "umbclogo.png", width=100)


#is user logged into umbc
if st.user.is_logged_in:
    userInfoDict = st.user.to_dict()
    name = userInfoDict["name"]
    email = userInfoDict["email"]
    picture = userInfoDict["picture"]

    with st.container():
        
        left, right = st.columns([4, 2])

        with left:
            st.markdown("### Account")
            st.markdown(f"**Welcome, {name}**")
            st.write(f"**Email:** {email}")
            st.write("You are authenticated through Google.")

        with right:
            st.image(ASSETS_DIR / "library1.jpg", width=100000)

       

else:
    st.info("Please sign in to access UMBC dashboard features.")

st.markdown("---")
st.subheader("Navigation")

col1, col2 = st.columns(2)

with col1:
    if st.user.is_logged_in is False:
        if st.button("Login", use_container_width=True):
            st.switch_page("pages/login_page.py")

    if st.user.is_logged_in is True:        
        if st.button("Books Page", use_container_width=True) and st.user.is_logged_in:
            st.switch_page("pages/books_page.py")

    if st.user.is_logged_in is True:
        if st.button("Room Reservations", use_container_width=True):
            st.switch_page("pages/room_reservations_page.py")

    if st.user.is_logged_in is True:
        if st.button("Upcoming Events", use_container_width=True):
            st.switch_page("pages/upcoming_events_page.py")

with col2:
    if st.button("Feedback Form", use_container_width=True):
        st.switch_page("pages/feedback_page.py")

    if st.user.is_logged_in is True:
        if st.button("Log out", use_container_width=True):
            st.logout()
