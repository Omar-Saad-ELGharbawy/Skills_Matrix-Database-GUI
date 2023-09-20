import streamlit as st
# from streamlit.hashing import _CodeHasher
# from streamlit.report_thread import get_report_ctx
# from streamlit.server.server import Server

# Define valid credentials
valid_credentials = {
    'admin': 'admin123',
    'employee': 'employee123'
}

# Define the admin page
def admin_page():
    st.title('Admin Page')
    # Add functionality for the admin page here

# Define the employee page
def employee_page():
    st.title('Employee Page')
    # Add functionality for the employee page here

# Define the login page
def login_page():
    st.title('Login Page')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if username in valid_credentials and password == valid_credentials[username]:
            # Store the user's role in a session variable
            # session_state = st.get(role='')
            session_state.role = 'admin' if username == 'admin' else 'employee'

# Check the user's role and display the appropriate page
session_state = st.get(role='')
if session_state.role == '':
    login_page()
elif session_state.role == 'admin':
    admin_page()
else:
    employee_page()