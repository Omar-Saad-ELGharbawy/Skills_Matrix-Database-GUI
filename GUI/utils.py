import streamlit as st
import pandas as pd

from GUI.database_queries import *
from utils import *


def edit_user(df):
    st.subheader("Edit Dataframe")
    row_index = st.selectbox("Row Index", df['ID'].values)

    column = st.selectbox("Column", df.columns)
    new_value = st.text_input("New Value")
    # add button save
    if st.button("Save Changes"):
        update_emp(column,new_value,row_index)
        st.experimental_rerun()

def add_user(df):
    st.subheader("Add Row")
    new_row = {}
    for column in df.columns:
        new_value = st.text_input(column)
        new_row[column] = new_value
    if st.button("Add Row"):
        result_tuple = (
        new_row.get('ID', ''),
        new_row.get('Name', ''),
        new_row.get('Password', ''),
        new_row.get('Department', ''),
        new_row.get('Position', '')
        )
        insert_emp(result_tuple)
        st.experimental_rerun()


def present_skills(userId):
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
                insert_skill(skill_data)
                # print("Inserted")
                st.experimental_rerun()

def view_user_page(userId):
    # display the user name in the page
    (Name,Department,Position) =  get_emp(userId)
    # presnet name department position in different columns
    # make title and header in middle of screen
    st.markdown("<h1 style='text-align: center; color:#083D77;'>"+"Skills Page"+"</ h1>", unsafe_allow_html=True)

    # st.title("Skills Page")
    # st.markdown("<h1 style='text-align: center; color:#083D77;'>"+str(Name)+"</ h1>", unsafe_allow_html=True)
    st.header(f'Welcome {Name}')
    # insert line
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Department : {Department}")
    with col2:
        st.write(f"Position : {Position}")

    # insert line
    st.markdown("---")

    # write Ahmed Skills in the middle of screen
    st.markdown("<h3 style='text-align: center; color:#083D77;'>"+str(Name)+" Skills"+"</ h3>", unsafe_allow_html=True)
    
    present_skills(userId)

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        new_category = st.text_input('Enter a Category:')
    with col2:
        new_skill = st.text_input('Enter a skill:')

    new_category_bt = st.button('Enter a new category')
    if new_category_bt:
        print("Pressed")
        print(new_category)
        print(new_skill)
        skill_data=(new_skill, new_category, userId)
        insert_skill(skill_data)
        print("Inserted")
        st.experimental_rerun()




def view_employees_skills():
    # Load employees data
    employees_data = get_all_emp()

    # Load skills data
    # skills_data = get_all_skills()

    # Set Streamlit app title
    st.title('Employee Skills Visualization')

    # Create a sidebar to select an employee
    employee_ids = employees_data['ID'].tolist()

    selected_employee = st.sidebar.selectbox('Select an employee:', employee_ids)

    st.subheader(f'Skills for {selected_employee}')
    # st.write(filtered_data[['Skill_Name', 'Skill_Type']])
    present_skills(selected_employee)



def logout():
    st.session_state.role = ""