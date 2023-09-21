import streamlit as st
import pandas as pd
import numpy as np

import mysql.connector

from utils import *

from emp_Page import *

host = 'localhost'
username = 'root'
database_password = '6@Monamo'
database = 'skills_matrix'

old_database ='skills_database'

st.set_page_config(
    page_title="Skiils Matrix",
    page_icon="📈",
    layout="wide"
)

mydb = mysql.connector.connect(
    host=host,
    user=username,
    passwd=database_password,
    database=database
)



mycursor = mydb.cursor()
print("Connected")
# Sidebar options
options = ['Admin Page', 'Users Skills', 'All Users']
selected_option = st.sidebar.selectbox("Select an option", options)

admin_ID = "Ahmed Galal01"

def view_employees():
    # Load employees data
    employees_data = pd.read_sql('SELECT * FROM employees', mydb)

    # Load skills data
    skills_data = pd.read_sql('SELECT * FROM skills', mydb)

    # Merge employees and skills data on the 'ID' column
    merged_data = employees_data.merge(skills_data, on='ID', how='inner')

    # Set Streamlit app title
    st.title('Employee Skills Visualization')

    # Create a sidebar to select an employee
    employee_id = employees_data['ID'].tolist()

    selected_employee = st.sidebar.selectbox('Select an employee:', employee_id)

    st.subheader(f'Skills for {selected_employee}')
    # st.write(filtered_data[['Skill_Name', 'Skill_Type']])
    present_SKILLS(selected_employee)



# Main content based on selected option
if selected_option == 'Admin Page':
    print("1")
    employee_page(admin_ID)
elif selected_option == 'Users Skills':
    print("2")
    view_employees()
elif selected_option == 'All Users':
    print("3")
    employees_data = pd.read_sql('SELECT * FROM employees', mydb)
    st.table(employees_data)





