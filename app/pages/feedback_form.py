import streamlit as st

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
