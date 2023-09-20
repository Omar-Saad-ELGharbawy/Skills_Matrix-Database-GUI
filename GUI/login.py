import streamlit as st

# GUI
def get_login_data():
    user_id = st.text_input("Username")
    password = st.text_input("Password", type="password")
    return (user_id,password)

# DATABASE
def check_login(username,password):
    if user_id == :
    
    # if user id is found and passowrd is correct access is true else access is false
    access = True
    # if user is admin privillege is true else privillege is false
    privillege = True
    return (access,)
    

# submit_button = st.button("Login")

#     if submit_button:
#         if username == "example_user" and password == "example_password":
#             st.success("Login successful")
#             # Add your logic for what happens after successful login
#         else:
#             st.error("Invalid username or password")

def main():
    # Set a header using st.header()
    st.title("Login Page")
    st.header('Welcome to my app')
    login()

if __name__ == "__main__":
    main()