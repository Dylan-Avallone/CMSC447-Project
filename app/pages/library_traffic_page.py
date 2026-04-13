import streamlit as st
import pandas as pd
import sys
from pathlib import Path

PAGE_DIR = Path(__file__).resolve().parent
APP_DIR = PAGE_DIR.parent
PROJECT_ROOT = APP_DIR.parent
sys.path.append(str(PROJECT_ROOT))

from app.backend.get_db import get_db

st.set_page_config(page_title="Library Traffic", page_icon="🚪", layout="wide")

if not (hasattr(st.user, "is_logged_in") and st.user.is_logged_in):
    st.warning("You must be signed in to access this page.")
    if st.button("Go to Login"):
        st.switch_page("pages/login_page.py")
    if st.button("Back to Home", key="traffic_security"):
        st.switch_page("pages/home_page.py")
    st.stop()

db = get_db()

if st.button("Back to Home"):
    st.switch_page("pages/home_page.py")

st.title("Library Traffic")
st.caption("Gate counter analytics for library entrance volume and peak usage patterns.")

rows = db.get_library_entry_log()

df = pd.DataFrame(rows, columns=["Entry ID", "Entry Time", "Entry Count"])

if df.empty:
    st.info("No library traffic data available yet.")
    st.stop()

df["Entry Time"] = pd.to_datetime(df["Entry Time"])
df["Date"] = df["Entry Time"].dt.date
df["Hour"] = df["Entry Time"].dt.strftime("%I:%M %p")
df["Weekday"] = df["Entry Time"].dt.day_name()

today_df = df[df["Date"] == pd.Timestamp.today().date()]

entries_today = int(today_df["Entry Count"].sum()) if not today_df.empty else 0
avg_hourly = round(df["Entry Count"].mean(), 1)

if not today_df.empty:
    peak_row = today_df.loc[today_df["Entry Count"].idxmax()]
    peak_hour_today = peak_row["Hour"]
    peak_entries_today = int(peak_row["Entry Count"])
else:
    peak_hour_today = "N/A"
    peak_entries_today = 0

m1, m2, m3 = st.columns(3)
m1.metric("Entries Today", entries_today)
m2.metric("Peak Hour Today", peak_hour_today)
m3.metric("Average Hourly Entries", avg_hourly)

st.subheader("Daily Totals")
daily_totals = df.groupby("Date", as_index=False)["Entry Count"].sum()
st.dataframe(daily_totals, use_container_width=True, hide_index=True)

st.subheader("Hourly Traffic Log")
st.dataframe(
    df[["Date", "Hour", "Weekday", "Entry Count"]],
    use_container_width=True,
    hide_index=True
)

st.subheader("Peak Time by Day")
peak_by_day = df.loc[df.groupby("Date")["Entry Count"].idxmax()][["Date", "Hour", "Entry Count"]]
peak_by_day = peak_by_day.rename(columns={"Hour": "Peak Hour", "Entry Count": "Peak Entries"})
st.dataframe(peak_by_day, use_container_width=True, hide_index=True)