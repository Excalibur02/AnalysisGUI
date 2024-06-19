import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# Sample data
def data_upload():
    df_upload = pd.read_csv('C:/Users/Admin/Downloads/MOCK_DATA.csv')
    return df_upload


df = data_upload()

# Set up Streamlit app
st.title("Interactive Pivot Table with ag-Grid")


# Function to create grid options
def create_grid_options(pivot_columns=None):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(paginationAutoPageSize=True)  # Enable pagination
    gb.configure_side_bar()  # Add a sidebar
    gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)

    if pivot_columns:
        for col in pivot_columns:
            gb.configure_column(col, pivot=True)
        gb.configure_column('Values', aggFunc='sum')

    gridOptions = gb.build()
    gridOptions['pivotMode'] = bool(pivot_columns)  # Enable pivot mode if there are pivot columns
    return gridOptions


# Display the grid with initial full DataFrame
grid_response = AgGrid(
    df,
    gridOptions=create_grid_options(),
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode='AS_INPUT',
    fit_columns_on_grid_load=True,
    height=500,
    width=1000
)

# Extract selected pivot columns
pivot_columns = grid_response['data'].columns.tolist()

