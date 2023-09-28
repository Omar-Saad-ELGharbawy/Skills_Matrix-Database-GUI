import streamlit as st

from utils import *
from database.database_queries import *


# ###################################################################################
#                                       GUI Pages Handler                           #    
# ###################################################################################

#############################################################################
#                        Define the Login page                             #
#############################################################################
def login_page():
    """
    login_page Description :
    This function displays the login page and updates the user id and password entered by the user in the session state
    It is used to redirect users to thei pages
    """
    st.title('Login Page')
    userId, UserPass= get_login_data()
    st.session_state.user_id = userId
    st.session_state.user_pass = UserPass
    if st.button('Login'):
        # Check if user ID and Password is correct from database
        if validate_user(userId, UserPass):
            # get the user position from the database
            position = get_position(userId)
            # Store the user's role in a session variable
            st.session_state.role = position
            st.experimental_rerun()

#############################################################################
#                        Define the User page                             #
#############################################################################
def user_page(userId):
    # display the user name in the page
    (Name,Department,Position) =  get_emp(userId)
    st.markdown("<h1 style='text-align: center; color:#083D77;'>"+"Skills Page"+"</ h1>", unsafe_allow_html=True)
    st.header(f'Welcome {Name}')
    # insert line
    st.markdown("---")
    # Present Department and Position of the user
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Department : {Department}")
    with col2:
        st.write(f"Position : {Position}")
    # insert line
    st.markdown("---")
    # Prsent user Skills
    st.markdown("<h3 style='text-align: center; color:#083D77;'>"+str(Name)+" Skills"+"</ h3>", unsafe_allow_html=True)
    present_skills(userId)
    st.markdown("---")
    # user can add new category and add it to the database
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
        insert_skills_row(skill_data)
        print("Inserted")
        st.experimental_rerun()

#############################################################################
#                        Define the Admin page
#############################################################################
def admin_page(admin_ID):
    """
    admin_page Description :
    This function displays the admin page
    It is used to present the admin skills and redirect the Admin to different Sub Pages :
        1- Admin Page
        2- All Users Page
        3- Users Skills Page
    """
    st.title('Admin Page')
    # Admin Dashboard to select the sub pages
    options = ['Admin Page', 'All Users', 'Users Skills']
    selected_option = st.sidebar.selectbox("Select an option", options)
    if selected_option == 'Admin Page':
        user_page(admin_ID)
    elif selected_option == 'All Users':
        all_users_page()
    elif selected_option == 'Users Skills':
        all_users_skills_page()

#############################################################################
#                        Define the All Users page                          #
#############################################################################
def all_users_page():
    """
    all_users_page Description :
    This function displays the all users page 
    It is used to present the all users data and redirect the Admin to different Sub Pages :
        1- Display All Users
        2- Add User
        3- Edit User
    """
    # Load employees data
    employees_data = get_all_emp()
    options = ['Display All Users', 'Add User', 'Edit User']
    selected_option = st.sidebar.selectbox("Select an option", options)
    # Main content based on selected option
    if selected_option == 'Display All Users':
        # Dispaly all users data from the database to the Admin in table form
        st.table(employees_data)
    elif selected_option == 'Add User':
        # Add new user to the database
        add_user(employees_data)
        st.table(employees_data)
    elif selected_option == 'Edit User':
        # Edit user data in the database
        edit_user(employees_data)
        st.table(employees_data)

#############################################################################
#                        Define the All Users Skills Page                   #
#############################################################################
def all_users_skills_page():
    """
    all_users_skills_page Description :
    This function displays the all users skills page
    It is used to present the all users skills data and redirect the Admin to different Sub Pages :
        1- Display All Users Skills
        2- Add User Skill
        3- Edit User Skill 
    """
    # Load employees data
    employees_data = get_all_emp()
    # Set Streamlit app title
    st.title('Employee Skills Visualization')
    # Create a sidebar to select an employee
    employee_ids = employees_data['ID'].tolist()
    selected_employee = st.sidebar.selectbox('Select an employee:', employee_ids)
    st.subheader(f'Skills for {selected_employee}')
    # Present the selected user ID SKills
    user_page(selected_employee)
