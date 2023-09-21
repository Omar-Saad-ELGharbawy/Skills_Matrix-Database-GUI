from my_queries import *

from emp_Page import *

import streamlit as st
# import mysql.connector

host = 'localhost'
username = 'root'
database_password = '6@Monamo'
database = 'skills_matrix'


# GUI
def get_login_data():
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")
    return (user_id,password)

# Function to check if the user_id and password are valid in the database
def validate_user(user_id, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=database_password,
            database=database
        )
        cursor = connection.cursor()

        # Query to check if the user_id and password exist in the database
        query = "SELECT COUNT(*) FROM employees WHERE ID = %s AND Password = %s"
        cursor.execute(query, (user_id, password))
        result = cursor.fetchone()[0]
        print(result)

        connection.close()
        return result
    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")
        return -1
    

# Define the admin page
def admin_page():
    st.title('Admin Page')
    # Add functionality for the admin page here
    st.button('Logout', on_click=logout)
    

def logout():
    st.session_state.role = ""


# Define the login page
def login_page():
    st.title('Login Page')
    userId, UserPass= get_login_data()
    st.session_state.user_id = userId
    st.session_state.user_pass = UserPass

    if st.button('Login'):
        
        if validate_user(userId, UserPass):
            # Store the user's role in a session variable
            position = get_position(userId)
            # print(position[0])
            st.session_state.role = 'admin' if position == 'Team leader' else 'employee'
            st.experimental_rerun()
            # return(userId, UserPass)


def main():
    # Initialization of Session State attributes (time,uploaded_signal)
    if 'role' not in st.session_state:
        st.session_state.role =""
    if 'user_id' not in st.session_state:
        st.session_state.user_id =""
    if 'user_pass' not in st.session_state:
        st.session_state.user_pass =""

    userId=  st.session_state.user_id 
    # UserPass= st.session_state.user_pass 

    if st.session_state.role == '':
        login_page()
    elif st.session_state.role == 'admin':
        admin_page()
    else:
        employee_page(userId)

    # Set a header using st.header()
    
    

if __name__ == "__main__":
    main()