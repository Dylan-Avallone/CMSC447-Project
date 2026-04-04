import streamlit as st
from .db import DB

#@st.cache_resource
def get_db():
    return DB("library_data.db", ["Initializer Files/dropDashboardTables.sql",
                                                    "Initializer Files/createDashboardTables.sql",
                                                    "Initializer Files/loadStaticDashboardTables.sql"])