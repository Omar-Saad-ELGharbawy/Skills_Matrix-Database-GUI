import streamlit as st

from utils import *
from Presentation.database_queries import *
# from all_users import *

#############################################################################
#                        Define the employee page
#############################################################################
def employee_page(userId):
    view_user_page(userId)
    st.button('Logout', on_click=logout)

#############################################################################
#                        Define the Admin page
#############################################################################
def admin_page(admin_ID):
    st.title('Admin Page')
    options = ['Admin Page', 'Users Skills', 'All Users']
    selected_option = st.sidebar.selectbox("Select an option", options)
    # Main content based on selected option
    if selected_option == 'Admin Page':
        print("1")
        view_user_page(admin_ID)
    elif selected_option == 'Users Skills':
        print("2")
        view_employees_skills()
    elif selected_option == 'All Users':
        print("3")
        all_users_page()
    # Add functionality for the admin page here
    st.button('Logout', on_click=logout)   


#############################################################################
#                        Define the All Users page
#############################################################################
def all_users_page():
    # Load employees data
    employees_data = get_all_emp()
    options = ['Display All Users', 'Edit User', 'Add User']
    selected_option = st.sidebar.selectbox("Select an option", options)
    # Main content based on selected option
    if selected_option == 'Display All Users':
        st.table(employees_data)
    elif selected_option == 'Edit User':
        edit_user(employees_data)
        st.table(employees_data)
    elif selected_option == 'Add User':
        add_user(employees_data)
        st.table(employees_data)


