import sqlite3
import streamlit as st
import numpy as np
import pandas as pd

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.backend.get_db import get_db
db = None

def startup():
    db = get_db("library_data")

if st.button("Feedback Form"):
    st.switch_page("pages/feedback_page.py")

if st.button("Login"):
    st.switch_page("pages/login_page.py")