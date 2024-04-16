import pandas as pd
import streamlit as st
import sqlite3 as sql

from st_aggrid import AgGrid, GridOptionsBuilder, \
    ColumnsAutoSizeMode, GridUpdateMode

from shared_code.user_status import side_header
from shared_code.season_info import my_seasons
from shared_code.gen_ag import gen_ag

side_header()

if 'user' not in st.session_state:
    st.header("Please sign in to view season information")
else:
    seasons = my_seasons()
    selected = gen_ag(seasons['joined'],['seasonName','generation','isActive','isDrafting'])
    if len(selected['selected_rows']) > 0 :
        with sql.connect("./data/users.db") as conn:
            season_members = pd.read_sql(
                    f"""
                    SELECT l.userID, username
                    FROM logins l
                    INNER JOIN
                    seasonMembers r
                    ON r.userID = l.userID AND r.seasonID ={selected['selected_rows'][0]['seasonID']};
                    """,conn
                    )
        selected_members = gen_ag(season_members,['username'])

