import streamlit as st

from shared_code.user_status import side_header
from shared_code.round_robin import round_robin

side_header()

st.markdown("# UNDER CONSTRUCTION")

matches = []
matches.append(st.expander("## Week {}"))
matches[-1].markdown("""
| Competitor 1 | Competitor 2 | Winner |
| ---: | :--- | :---: |
| Charlotte | Nick | ??? |
| Paul      | Giuseppe | ??? |
| Dylan     | Kaysee | ??? |
| Joey      | Rance | ??? |
| BYE       | Justin | Justin |

""")
                     
robin_roll = st.button("Round Robin Test",
    # on_click=round_robin,
    # kwargs={'players':['jd','omg','lmao','gai']}
    )

players = [
    'KAYSEE',
    'GIUSEPPE',
    'CHARLOTTE',
    'JUSTIN',
    'DYLAN',
    'PAUL',
    'JOEY',
    'NICK',
    'RANCE',
    'JD'
]
if robin_roll:
    robin = round_robin(players)
    st.write(robin)
# st.write(fellas)