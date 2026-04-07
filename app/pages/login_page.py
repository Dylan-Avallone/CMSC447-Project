import streamlit as st
from app.backend.get_db import get_db

st.set_page_config(page_title="Login", page_icon="x", layout="centered")

# User tried to log in but is not authorized
if "invalid_user" in st.session_state:
    if st.session_state["invalid_user"]:
        st.error("You are not authorized to access the dashboard")
        st.session_state["displayed_error"] = True

# Title
st.title("Login")
st.caption("Sign in with your UMBC Google account.")

#home button
if st.button("Back to Home"):
    st.switch_page("pages/home_page.py")

#check if authenticated
auth_configured = hasattr(st.user, "is_logged_in")

if not auth_configured:
    st.warning("Google login is not configured yet.")
    st.code(
        """Create .streamlit/secrets.toml with your Google OAuth settings,
then restart Streamlit.""",
        language="toml"
    )
    st.stop()

if not st.user.is_logged_in:
    st.write("Use Google to sign in.")
    if st.button("Sign in with Google", use_container_width=True):
        st.login("google")
    st.stop()

db = get_db()
email = st.user.get("email", "")
name = st.user.get("name", "User")

# UMBC only
if not db.has_user(email):
    st.session_state["invalid_user"] = True
    if "displayed_error" in st.session_state:
        if not st.session_state["displayed_error"]:
            st.rerun()

st.success(f"Signed in as {name}")
st.write(f"Email: {email}")

col1, col2 = st.columns(2)

with col1:
    if st.button("Continue", use_container_width=True):
        st.switch_page("pages/home_page.py")

with col2:
    if st.button("Log out", use_container_width=True):
        st.logout()