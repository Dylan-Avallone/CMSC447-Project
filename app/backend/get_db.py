import streamlit as st
from .db import DB

@st.cache_resource
def get_db():
    return DB()