import streamlit as st

from shared_code.user_status import side_header

tmp_uname = st.text_input("TMP - Set Username")
t_uname = st.button("TEST UNAME")

if t_uname:
    st.session_state['user'] = tmp_uname

side_header()