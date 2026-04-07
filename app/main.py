import streamlit as st
from app.backend.room_availability_scraper import *

# scrape_hourly()

# When login is finished through google, the main script is rerun. Thus, the target should be the login page
st.switch_page("pages/login_page.py")