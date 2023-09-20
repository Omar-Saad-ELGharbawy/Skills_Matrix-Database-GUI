import streamlit as st



# Define the admin page
def admin_page():
    st.title('Admin Page')
    # Add functionality for the admin page here
    st.button('Logout', on_click=logout)
    