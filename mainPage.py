import streamlit as st

from database.database_queries import *
from pages_handler import *
from utils import *


#############################################################################
#                                   GUI                                    #
#############################################################################

# This is the main file of the GUI
# It contains the main function that :
    # 1- Initialize the session state attributes
    # 2- Set the page configuration
    # 3- Handles the Page View according to the login data using pages_handler file

def main():
    # Initialization of Session State attributes (time,uploaded_signal)
    if 'role' not in st.session_state:
        st.session_state.role =""
    if 'user_id' not in st.session_state:
        st.session_state.user_id =""
    if 'user_pass' not in st.session_state:
        st.session_state.user_pass =""
    # Set the page configuration
    st.set_page_config(
    page_title="Skiils Matrix",
    page_icon="📈",
    layout="wide"
    )
    userId=st.session_state.user_id 
    if st.session_state.role == '':
        # Initial login page 
        login_page()
    elif st.session_state.role == 'Admin':
        # Admin page if user position is admin
        admin_page(userId)
        st.button('Logout', on_click=logout)
    else:
        # User page if user position is not admin
        user_page(userId)
        st.button('Logout', on_click=logout)


if __name__ == "__main__":
    main()