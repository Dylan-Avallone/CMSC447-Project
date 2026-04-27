import streamlit as st
from pathlib import Path
import sys
import pandas as pd
from app.backend.get_db import get_db
from app.backend.user import User

PAGE_DIR = Path(__file__).resolve().parent
APP_DIR = PAGE_DIR.parent
PROJECT_ROOT = APP_DIR.parent
sys.path.append(str(PROJECT_ROOT))
db = get_db()

st.set_page_config(page_title="Book Management", page_icon="x", layout="wide")
st.title("Admin Controls")
st.caption("Add and remove users, change permissions.")

#home button
if st.button("Back to Home"):
    st.switch_page("pages/home_page.py")

# Sample Data
rows = db.get_printable_table("Users")
if 'base_df' not in st.session_state:
    st.session_state['base_df'] = pd.DataFrame(rows, columns=["ID", "Username", "Email", "Role"])

st.title("User Management")

# Configure the columns
edited_df = st.data_editor(
    st.session_state['base_df'],
    column_config={
        "Role": st.column_config.SelectboxColumn(
            help="Select the user's permission level",
            options=["admin", "user"],
            required=True,
        ),
        "ID": None
    },
    hide_index=True,
    num_rows="dynamic", # This adds a '+' and '-' button to add/delete rows
    key="edited_df"
)

if st.button("Save Changes"):
    changes = st.session_state['edited_df']
    changed_users = changes["edited_rows"]
    added_users = changes["added_rows"]
    deleted_users = changes["deleted_rows"]
    for row in added_users:
        added_user = added_users[row]
        db.add_user(User(row, added_user["Username"], added_user["Email"], added_user["Role"]))
    for row in deleted_users:
        deleted_user = deleted_users[row]
        db.remove_user(User(row, deleted_user["Username"], deleted_user["Email"], deleted_user["Role"]))
    for row in changed_users:
        changed_user = changed_users[row]
        changed_user_obj = User(row)
        for attr in changed_user:
            setattr(changed_user_obj, attr, changed_user[attr])
        db.edit_user(changed_user_obj)