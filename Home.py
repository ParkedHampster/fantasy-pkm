import streamlit as st
import pandas as pd

from shared_code.user_status import side_header

st.set_page_config(
        page_title="Home - Fantasy Pokemon League",
)

side_header()

if 'user' in st.session_state:
    st.title(
        st.session_state['user'].upper()
        )
    st.header("Team:")
    st.table(
        pd.DataFrame(
            [{
                'Name':'UNDER CONSTRUCTION'
            }]
        ))
else:
    st.title(
        "Please Sign in to View Personal Stats"
    )