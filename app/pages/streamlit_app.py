import streamlit as st
import pandas

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("UMBC Library Dashboard")
st.write("dashboard example data.")

# just example data
data = pandas.DataFrame({
    "Category": ["Visitors", "Checkouts", "Reservations"],
    "Count": [120, 75, 32]
})

st.subheader("Sample Data")
st.dataframe(data)

st.subheader("Sample Chart")
st.bar_chart(data.set_index("Category"))