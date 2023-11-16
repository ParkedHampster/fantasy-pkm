import pandas as pd
import streamlit as st
import sqlite3 as sql

from st_aggrid import AgGrid, GridOptionsBuilder, \
    ColumnsAutoSizeMode, GridUpdateMode

from shared_code.user_status import side_header
from shared_code.season_info import my_seasons

side_header()

if 'user' not in st.session_state:
    st.header("Please sign in to view season information")
else:
    seasons = my_seasons()
    gb = GridOptionsBuilder.from_dataframe(
            seasons['joined'][['seasonName','generation','isActive','isDrafting']]
            )
    gb.configure_selection(selection_mode='single',use_checkbox=True)
    gb.configure_pagination(
            enabled=True,
            paginationAutoPageSize=False,
            paginationPageSize=10
            )

    gridOptions = gb.build()
    with st.container():
        st.header("Select Season to work with")
        selected = AgGrid(
                seasons['joined'],
                gridOptions=gridOptions,
                columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
                fit_columns_on_grid_load=True,
                enable_enterprise_modules=False,
                update_mode=GridUpdateMode.SELECTION_CHANGED
                )
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
            gb = GridOptionsBuilder.from_dataframe(
                    season_members[['username']]
                    )
            gb.configure_selection(selection_mode='single',use_checkbox=True)
            gb.configure_pagination(
                    enabled=True,
                    paginationAutoPageSize=False,
                    paginationPageSize=10
                    )

            gridOptions = gb.build()
            selected_members = AgGrid(
                    season_members,
                    gridOptions=gridOptions,
                    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
                    fit_columns_on_grid_load=True,
                    enable_enterprise_modules=False,
                    update_mode=GridUpdateMode.SELECTION_CHANGED
                    )

