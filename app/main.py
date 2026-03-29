import sqlite3
import streamlit as st
import numpy as np
import pandas as pd

if st.button("Feedback Form"):
    st.switch_page("pages/feedback_form.py")