import streamlit as st
import mysql.connector

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
            host='your_mysql_host',
            user='your_mysql_user',
            password='your_mysql_password',
            database='your_mysql_database'
        )
        cursor = connection.cursor()

        # Query to check if the user_id and password exist in the database
        query = "SELECT COUNT(*) FROM employees WHERE user_id = %s AND password = %s"
        cursor.execute(query, (user_id, password))
        result = cursor.fetchone()[0]

        connection.close()
        return result
    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")
        return -1
    
# DATABASE
# def check_login(user_id,password):    
#     # if user is admin privillege is true else privillege is false
#     if user_id == "SELECT position FROM employees":
#         privillege = True
#     else:
#         privillege = False
#     # if user id is found and passowrd is correct access is true else access is false
#     if password == "SELECT password FROM employees":
#         access = True
#     else:
#         access = False

    # return (access,privillege)


    

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
    userId, UserPass= get_login_data()
    validate_user(userId, UserPass)

if __name__ == "__main__":
    main()