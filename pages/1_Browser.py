import pandas as pd
import streamlit as st
import sqlite3 as sql

from st_aggrid import AgGrid, GridOptionsBuilder, \
    ColumnsAutoSizeMode, GridUpdateMode

from shared_code.user_status import side_header

def team_clear():
    del st.session_state['team']

def register_team():
    with sql.connect('./data/users.db') as conn:
        cursor = conn.cursor()
        for pkm in st.session_state['team']:
            cursor.execute(f"""
                INSERT INTO teams
                (
                userID, pkmName, pkmEvoStage
                )
                VALUES
                (
                '{
                    st.session_state['userID']
                }','{
                    pkm['Name']
                }','{
                    pkm['Stage']
                }'
                )
                """)
        team_clear()


side_header()

st.sidebar.title("Team Builder")

pkm_dex = pd.read_csv('./data/pkm_base.tsv',sep='\t')
gen_max = pd.read_csv('./data/gen_max.tsv',sep='\t')

curr_gen = int(
    st.number_input("Current Generation",
        min_value=1,
        value=4,
        max_value=9
    )
    )

act_dex = pkm_dex[
        pkm_dex['Number'] <=
        gen_max[
            gen_max['gen'] == curr_gen
            ]['max'].iloc[0]
        ]

typelist = [
    '',
    'Normal',
    'Fire',
    'Water',
    'Grass',
    'Electric',
    'Ice',
    'Fighting',
    'Poison',
    'Ground',
    'Flying',
    'Psychic',
    'Bug',
    'Rock',
    'Ghost',
    'Dark',
    'Dragon',
    'Steel',
    'Fairy',
]

st.title("Fantasy Pokemon League")
st.header("Pokemon Browser")

pk_name_search = st.text_input("Pokemon Name")

type_cols = st.columns(2)

with type_cols[0]:
    type1 = st.selectbox(
        "Type 1",
        typelist
    )

with type_cols[1]:
    type2 = st.selectbox(
        "Type 2",
        typelist
    )

queried_dex = act_dex[
    (act_dex['Name'].str.contains(pk_name_search,na=False,case=False)) &
    (
        (act_dex['Type 1'].str.contains(type1,na=False)) |
        (act_dex['Type 2'].str.contains(type1,na=False))
    ) &
    (
        (act_dex['Type 1'].str.contains(type2,na=False)) |
        (act_dex['Type 2'].str.contains(type2,na=False))
    )
    ]

selector = st.button("Add Selected")


gb = GridOptionsBuilder.from_dataframe(
    queried_dex[['Number','Name','Type 1','Type 2','Stage']]
    )
gb.configure_selection(selection_mode='single',use_checkbox=True)
gb.configure_pagination(
    enabled=True,
    paginationAutoPageSize=False,
    paginationPageSize=25,
)

gridOptions = gb.build()
with st.container():
    selected = AgGrid(
        queried_dex[['Number','Name','Type 1','Type 2','Stage']],
        gridOptions=gridOptions,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        fit_columns_on_grid_load=True,
        enable_enterprise_modules=False,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        )

with st.sidebar:
    btn_cols = st.columns(2)
    with btn_cols[0]:
        clear_team = st.button(":red[Clear Team]",
        use_container_width=True,
        on_click=team_clear
        )
    with btn_cols[1]:
        delete_selected = st.button("Delete Selected",
        use_container_width=True
        )

if selector:
    try:
        st.session_state['team'].append(
            selected['selected_rows'][0]
        )
    except:
        st.session_state['team'] = selected['selected_rows']

if 'team' not in st.session_state:
    st.session_state['team'] = ''
else:
    try:
        st.sidebar.dataframe(
            pd.DataFrame(
                st.session_state['team']
            )[
                ['Number','Name','Stage']
            ].set_index('Number'),
            use_container_width=True
        )
    except:
        pass

if 'user' in st.session_state:
    with st.sidebar:
        st.button("Submit Team",
            use_container_width=True,
            on_click=register_team
            )
        # st.write(
        #     st.session_state
        # )