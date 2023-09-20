import streamlit as st
import mysql.connector

host = 'localhost'
username = 'root'
database_password = '6@Monamo'
database = 'skills_database'

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
    

# Define the employee page
def employee_page():
    st.title('Employee Page')
    # display the user name in the page
    st.write(f"Welcome {st.session_state.user_id}")
    # Add functionality for the employee page here
    st.button('Logout', on_click=logout)

def logout():
    st.session_state.role = ""

def group_by(user_id):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        user=username,
        password=database_password,
        database=database
    )
    cursor = connection.cursor()

    query = """ SELECT Skill_Type, GROUP_CONCAT(Skill_Name) AS skill_names
                FROM skills
                WHERE id = %s
                GROUP BY Skill_Type;"""
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    connection.close()
    return result

# Define the login page
def login_page():
    st.title('Login Page')
    userId, UserPass= get_login_data()
    st.session_state.user_id = userId
    st.session_state.user_pass = UserPass

    if st.button('Login'):
        
        if validate_user(userId, UserPass):
            # Store the user's role in a session variable
            st.session_state.role = 'admin' if username == 'admin' else 'employee'
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

    if st.session_state.role == '':
        login_page()
    elif st.session_state.role == 'admin':
        admin_page()
    else:
        employee_page()

    # Set a header using st.header()
    
    

if __name__ == "__main__":
    main()