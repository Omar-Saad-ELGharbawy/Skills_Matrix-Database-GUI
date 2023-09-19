import streamlit as st
import pandas as pd


def display_dataframe(df):
    # st.dataframe(df)
    st.table(df)


def edit_dataframe(df):
    st.subheader("Edit Dataframe")
    row_index = st.number_input("Row Index", min_value=0, max_value=len(df)-1, step=1)
    column = st.selectbox("Column", df.columns)
    new_value = st.text_input("New Value", df.loc[row_index, column])
    df.loc[row_index, column] = new_value

def add_row(df):
    st.subheader("Add Row")
    new_row = {}
    for column in df.columns:
        new_value = st.text_input(column)
        new_row[column] = new_value
    # adding a row
    df.loc[len(df.index)] = new_row  


def save_changes(df, data_Path) :
    # Save dataframe to CSV
    if st.button("Save Changes"):
        df.to_csv(data_Path, index=False)
        st.success("Dataframe saved to Skills.csv")

