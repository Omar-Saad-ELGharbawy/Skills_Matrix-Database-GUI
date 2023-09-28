import streamlit as st
import pandas as pd

from database.database_queries import *

def get_login_data():
    """
    get_login_data Description :
    This function returns the user id and password entered by the user
    """
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")
    return (user_id,password)

def logout():
    # Returns the user to the main login page
    st.session_state.role = ""

def present_skills(userId):
    """
    present_skills Description :
    This function displays the user skills
    It enables the user to add new skill to each category and add it to the database
    """
    # group skills from database by each category to present it in the GUI Page
    skills = group_by(userId)
    columns = st.columns(len(skills))
    # loop over skills and get tuple and number of element
    for i, data in enumerate(skills):
        # Extract the category and skills from the tuple
        category, skills = data
        # Split the skills into a list
        skill_list = skills.split(',')
        # Create a dataframe from the skill list
        df = pd.DataFrame(skill_list, columns=["Category"])
        with columns[i]:
            st.subheader(category)
            st.write(df)
            # Add skill button and input field
            new_skill = st.text_input(f'Enter a {category} skill:')
            if (st.button(f'Add {category} Skill') and new_skill ):
                # print("Pressed")
                # print(new_skill)
                skill_data=(new_skill, category, userId)
                insert_skills_row(skill_data)
                # print("Inserted")
                st.experimental_rerun()

def add_user(df):
    """
    add_user Description :
    This function enables the user to add new row to the dataframe
    """
    st.subheader("Add Row")
    new_row = {}
    for column in df.columns:
        new_value = st.text_input(column)
        new_row[column] = new_value
    # Add row button to submit changes to the database
    if st.button("Add Row"):
        result_tuple = (
        new_row.get('ID', ''),
        new_row.get('Name', ''),
        new_row.get('Password', ''),
        new_row.get('Department', ''),
        new_row.get('Position', '')
        )
        insert_employee_row(result_tuple)
        st.experimental_rerun()

def edit_user(df):
    """
    edit_user Description :
    This function enables the user to edit the data in the dataframe
    """
    st.subheader("Edit Dataframe")
    row_index = st.selectbox("Row Index", df['ID'].values)
    column = st.selectbox("Column", df.columns)
    new_value = st.text_input("New Value")
    # Save button to submit changes to the database
    if st.button("Save Changes"):
        update_emp(column,new_value,row_index)
        st.experimental_rerun()

