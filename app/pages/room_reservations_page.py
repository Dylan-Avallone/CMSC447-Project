import streamlit as st
import pandas as pd
import sys
from pathlib import Path
from datetime import date
from app.backend.get_db import get_db
from app.backend.table_function_classes.db_roomreservation_functions import DBRRFunctions

if not (hasattr(st.user, "is_logged_in") and st.user.is_logged_in):
    st.warning("You must be signed in to access this page.")
    if st.button("Go to Login"):
        st.switch_page("pages/login_page.py")
    if st.button("Back to Home", key="security"):
            st.switch_page("pages/home_page.py")
    st.stop()
    

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))

st.set_page_config(
    page_title="Room Reservations",
    page_icon="x",
    layout="wide"
)

db = get_db()
rr_functions = DBRRFunctions(db)

#home button
if st.button("Back to Home"):
    st.switch_page("pages/home_page.py")

#title
st.title("Room Reservations")
st.caption("Monitor past, current, and upcoming reservations across library rooms.")



# -----------------------------
# Data loading

rr_functions.refresh_data()
rows = rr_functions.get_reservations()

df = pd.DataFrame([rr.to_row() for rr in rows])

if df.empty:
    st.info("No reservation data available yet.")
    st.stop()

# -----------------------------
# Cleanup / formatting

df["start_time"] = df["start_time"].astype(str).str[:5]
df["end_time"] = df["end_time"].astype(str).str[:5]

today = date.today()

def classify_period(reservation_date):
    """
    :param reservation_date:
    :return:
    """
    if reservation_date < today:
        return "Past"
    elif reservation_date == today:
        return "Today"
    return "Future"

df["Period"] = df["reservation_date"].apply(classify_period)

# -----------------------------
# Top metrics

total_reservations = len(df)
past_count = len(df[df["Period"] == "Past"])
today_count = len(df[df["Period"] == "Today"])
future_count = len(df[df["Period"] == "Future"])

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total", total_reservations)
m2.metric("Past", past_count)
m3.metric("Today", today_count)
m4.metric("Upcoming", future_count)

st.markdown("---")

# -----------------------------
# Filters

st.subheader("Filters")

c1, c2, c3 = st.columns(3)

with c1:
    search_text = st.text_input(
        "Search by person or purpose",
        placeholder="e.g. study group, Ava Johnson"
    )

with c2:
    period_filter = st.selectbox(
        "Timeframe",
        ["All", "Past", "Today", "Future"]
    )

with c3:
    room_options = ["All"] + sorted(df["room_id"].dropna().unique().tolist())
    room_filter = st.selectbox("Room", room_options)

filtered_df = df.copy()

if search_text:
    q = search_text.strip().lower()
    filtered_df = filtered_df[
        filtered_df["Reserved By"].str.lower().str.contains(q, na=False) |
        filtered_df["Purpose"].str.lower().str.contains(q, na=False)
    ]

if period_filter != "All":
    filtered_df = filtered_df[filtered_df["Period"] == period_filter]

if room_filter != "All":
    filtered_df = filtered_df[filtered_df["Room"] == room_filter]

filtered_df = filtered_df.sort_values(
    by=["reservation_date", "start_time", "room_id"],
    ascending=[True, True, True]
)


# -----------------------------
# Main reservation table

st.subheader("Reservation Timeline")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# -----------------------------
# Sectioned views

st.markdown("---")
st.subheader("Grouped Views")

tab1, tab2, tab3 = st.tabs(["Today", "Upcoming", "Past"])

with tab1:
    today_df = df[df["Period"] == "Today"].sort_values(by=["start_time", "room_id"])
    if today_df.empty:
        st.info("No reservations scheduled for today.")
    else:
        st.dataframe(today_df, use_container_width=True, hide_index=True)

with tab2:
    future_df = df[df["Period"] == "Future"].sort_values(by=["reservation_date", "start_time"])
    if future_df.empty:
        st.info("No upcoming reservations.")
    else:
        st.dataframe(future_df, use_container_width=True, hide_index=True)

with tab3:
    past_df = df[df["Period"] == "Past"].sort_values(by=["reservation_date", "start_time"], ascending=[False, False])
    if past_df.empty:
        st.info("No past reservations found.")
    else:
        st.dataframe(past_df, use_container_width=True, hide_index=True)