import streamlit as st
from .db import DB

#@st.cache_resource
def get_db(name):
    initializer_files = ["dropDashboardTables.sql", "createDashboardTables.sql", "loadStaticDashboardTables.sql"]
    return DB(name, initializer_files)