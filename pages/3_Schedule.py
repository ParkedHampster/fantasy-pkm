import streamlit as st
import sqlite3 as sql
import pandas as pd

from shared_code.user_status import side_header
from shared_code.round_robin import round_robin

side_header()

st.markdown("# UNDER CONSTRUCTION")

# matches = []
# matches.append(st.expander("## Week {}"))
# matches[-1].markdown("""
# | Competitor 1 | Competitor 2 | Winner |
# | ---: | :--- | :---: |
# | Charlotte | Nick | ??? |
# | Paul      | Giuseppe | ??? |
# | Dylan     | Kaysee | ??? |
# | Joey      | Rance | ??? |
# | BYE       | Justin | Justin |

# """)
                     
robin_roll = st.button("Round Robin Test",
    # on_click=round_robin,
    # kwargs={'players':['jd','omg','lmao','gai']}
    )

# players = [
#     'KAYSEE',
#     'GIUSEPPE',
#     'CHARLOTTE',
#     'JUSTIN',
#     'DYLAN',
#     'PAUL',
#     'JOEY',
#     'NICK',
#     'RANCE',
#     'JD'
# ]
if robin_roll:
    conn = sql.connect('./data/users.db')
    players = list(pd.read_sql(
        """
        SELECT username FROM logins
        """,conn
    )['username'])
    matches = round_robin(players)
    # st.dataframe(matches[0])
    match_list = []
    for i, match in enumerate(matches):
        match_list.append(st.expander(f"Week {i+1}"))
        match_list[i].dataframe(
            match
        )


# st.write(fellas)