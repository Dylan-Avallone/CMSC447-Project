import streamlit as st
from app.backend.room_availability_scraper import *

scrape_hourly()

st.switch_page("pages/home_page.py")