import pandas as pd
import streamlit as st

from st_aggrid import AgGrid, GridOptionsBuilder, \
    ColumnsAutoSizeMode, GridUpdateMode

def gen_ag(df,cols):
    gb = GridOptionsBuilder.from_dataframe(
            df[cols]
            )
    gb.configure_selection(selection_mode='single',use_checkbox=True)
    gb.configure_pagination(
            enabled=True,
            paginationAutoPageSize=False,
            paginationPageSize=10
            )

    gridOptions = gb.build()
    return AgGrid(
            df,
            gridOptions=gridOptions,
            columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
            fit_columns_on_grid_load=True,
            enable_enterprise_modules=False,
            update_mode=GridUpdateMode.SELECTION_CHANGED
            )
