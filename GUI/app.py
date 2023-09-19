import streamlit as st
import pandas as pd
# import numpy as np

from utils import display_dataframe, edit_dataframe, add_row , save_changes

data_Path = "..\Data\Skills.csv"
df = pd.read_csv(data_Path)
# st.table(df)
# st.dataframe(data)

# Sidebar options
options = ['Display Dataframe', 'Edit Dataframe', 'Add Row']
selected_option = st.sidebar.selectbox("Select an option", options)

# Main content based on selected option
if selected_option == 'Display Dataframe':
    display_dataframe(df)
elif selected_option == 'Edit Dataframe':
    edit_dataframe(df)
    display_dataframe(df)
    save_changes(df, data_Path)
elif selected_option == 'Add Row':
    add_row(df)
    display_dataframe(df)
    save_changes(df, data_Path)



