import datetime
import numpy as np
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder


def data_upload():
    df_upload = pd.read_csv('C:/Users/Admin/Downloads/MOCK_DATA.csv')
    return df_upload


df = data_upload()

st.header("AgGrid table")
gb = GridOptionsBuilder()

# makes columns resizable, sortable and filterable by default
gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=False,
)

# configures state column to have a 80px initial width
gb.configure_column(field="day", header_name="Day", width=80)

gb.configure_column(
    field="month",
    header_name="Month",
    flex=1,
    width=350,
    tooltipField="month",
)

gb.configure_column(field="request", header_name="Request", width=100, type=["numericColumn"])

gb.configure_column(field="type", header_name="Type", width=100)

# makes tooltip appear instantly
gb.configure_grid_options(tooltipShowDelay=0)
go = gb.build()

AgGrid(data=df, gridOptions=go, height=400)
