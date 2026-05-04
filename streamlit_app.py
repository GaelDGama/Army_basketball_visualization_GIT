import streamlit as st

pg = st.navigation([st.Page("Players.py"),st.Page("Teams.py")])
pg.run()