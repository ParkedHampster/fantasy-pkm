import streamlit as st

from shared_code.user_status import side_header

side_header()

season_status = st.container()
season_status.write("Test")
