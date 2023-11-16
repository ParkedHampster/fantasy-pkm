import streamlit as st
import pandas as pd
import sqlite3 as sql

def my_seasons():
    with sql.connect("./data/users.db") as conn:
        joined_seasons = pd.read_sql(
                f"""
                SELECT 
                    l.seasonID, seasonName, seasonAdminID, isActive,
                    isDrafting, generation, seasonWinner, seasonWinnerID
                FROM seasonData l
                INNER JOIN
                seasonMembers r
                ON l.seasonID = r.seasonID AND r.userID = {st.session_state['userID']};
                """,conn)
        owned_seasons = joined_seasons[joined_seasons['seasonAdminID'] == st.session_state['userID']]
        return {'owned':owned_seasons,'joined':joined_seasons}

