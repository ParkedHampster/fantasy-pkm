import pandas as pd
import streamlit as st

st.set_page_config(
        page_title="Fantasy Pokemon League",
)

st.sidebar.title("Pokemon Browser")

pkm_dex = pd.read_csv('./data/pkm_base.tsv',sep='\t',index_col=0)
gen_max = pd.read_csv('./data/gen_max.tsv',sep='\t')

curr_gen = int(
    st.number_input("Current Generation",
        min_value=1,
        value=4,
        max_value=9
    )
    )

act_dex = pkm_dex[
        pkm_dex.index <=
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



act_dex[
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