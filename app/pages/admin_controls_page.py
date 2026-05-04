import streamlit as st
from pathlib import Path
import sys
import pandas as pd
from app.backend.get_db import get_db
from app.backend.table_object_classes.user import User

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

    actions = {
        "add": (added_users, db.add_user),
        "remove": (deleted_users, db.remove_user),
        "edit": (changed_users, db.edit_user)
    }
    for action_name, (user_group, db_method) in actions.items():
        for row_id, data in user_group.items():
            user_obj = User.from_row(data)  # Assuming you add this method
            db_method(user_obj)