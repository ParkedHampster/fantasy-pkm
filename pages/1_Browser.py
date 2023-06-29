import pandas as pd
import streamlit as st

from st_aggrid import AgGrid, GridOptionsBuilder, \
    ColumnsAutoSizeMode, GridUpdateMode

st.set_page_config(
        page_title="Fantasy Pokemon League",
)

st.sidebar.title("Team Builder")

pkm_dex = pd.read_csv('./data/pkm_base.tsv',sep='\t')#,index_col=0)
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


gb = GridOptionsBuilder.from_dataframe(queried_dex)
gb.configure_selection(selection_mode='single',use_checkbox=True)
gridOptions = gb.build()

selected = AgGrid(queried_dex,
    gridOptions=gridOptions,
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
    enable_enterprise_modules=False,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
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
    st.sidebar.write(
        pd.DataFrame(
            st.session_state['team']
        )[
            ['Number','Name']
        ].set_index('Number')
    )