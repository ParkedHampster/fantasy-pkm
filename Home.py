import streamlit as st
import pandas as pd
import sqlite3 as sql

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
    with sql.connect('./data/users.db') as conn:
        query = f"""
        SELECT * FROM teams
        WHERE userID = '{
            st.session_state['userID']
        }'
        """
        teams_df = pd.read_sql(query,conn)
    st.dataframe(
        teams_df[
            ['pkmName','pkmEvoStage']
            ].reset_index(drop=True).rename(
                columns={
                    'pkmName':'Pokemon',
                    'pkmEvoStage':'Stage'
                }
            ),
            use_container_width=True,
            hide_index=True
        )
else:
    st.title(
        "Please Sign in to View Personal Stats"
    )