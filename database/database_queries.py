import mysql.connector
import streamlit as st
import pandas as pd

from database_connection import *

""" 
database_queries File Documentation :
    This file contains all the queries that are used with the GUI to interact with the database.
    The queries are used to insert, update, and retrieve data from the database.
    The queries are used in the following files:
        - GUI/mainPage.py
        - GUI/pages_handler.py
        - GUI/utils.py
    The queries are :
        - validate_user(user_id, userPassword)
        - insert_employee_row(user_data)
        - update_emp(column_to_update,new_value,specific_id)
        - insert_skills_row(user_data)
        - insert_emp(user_data)
        - insert_skill(user_data)
        - get_emp(user_id)
        - get_position(user_id)
        - group_by(user_id)
        - get_all_emp()
        - get_all_skills()
"""

# Function to establish a database connection
def connect_to_database(host, username, password, database):
    mydb = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    # if mydb.is_connected():
    #     print('Connected to the database')
    # else:
    #     print('Failed to connect to the database')
    return mydb

# Function to check if the user_id and password are valid in the database
def validate_user(user_id, userPassword):
    """
    validate_user Desribtion :
    This function checks if the user_id and password exist in the database.
    If successful, it returns the number of rows that match the query (1 or 0)
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    user_id : string
        The id of the employee
    userPassword : string
        The password of the employee
    Returns
    -------
    result : int
        1 if login parameters is valid
        0 if login parameters is invalid
    """
    try:
        # Connect to the MySQL database
        connection = connect_to_database(host, username, password, database)
        cursor = connection.cursor()
        # Query to check if the user_id and password exist in the database
        query = "SELECT COUNT(*) FROM employees WHERE ID = %s AND Password = %s"
        cursor.execute(query, (user_id, userPassword))
        result = cursor.fetchone()[0]
        print(result)
        connection.close()
        return result
    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")
        return -1


def insert_employee_row(employee_data):
    """
    insert_employee_row Desribtion :
    This function inserts a row in the employees table in the database.
    If successful, it prints "Row Inserted" on console
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    employee_data : tuple
        A tuple containing the data to be inserted in the row in this format :
        (ID, Name, Password, Department, Position)
    Returns None
    -------
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    try:
        query = """
        INSERT INTO employees (ID, Name, Password, Department, Position)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query,employee_data)
        connection.commit()
        connection.close()
    except mysql.connector.Error as error:
        if error.errno == 1062:
            print("Duplicate entry error: This username already exists.")
    else:
        print("An error occurred:", error)

def insert_skills_row(skills_data):
    """ 
    insert_skills_row Desribtion :
    This function inserts a row in the skills table in the database.
    If successful, it prints "Row Inserted" on console
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    skills_data : tuple
        A tuple containing the data to be inserted in the row in this format :
        (Skill_Name, Skill_Type, ID)
    Returns None
    -------
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    try:
        query = """
        INSERT INTO `skills` (`Skill_Name`,  `Skill_Type`, `ID`) 
        VALUES (%s, %s, %s)
        """
        # Execute the SQL query
        cursor.execute(query,skills_data)
        # Commit the changes and close the connection
        connection.commit()
        connection.close()
    except mysql.connector.Error as error:
        if error.errno == 1062:
            print("Duplicate entry error: This username already exists.")
    else:
        print("An error occurred:", error)


def update_emp(column_to_update,new_value,specific_id):
    """
    update_emp Desribtion :
    This function updates a row in the employees table in the database.
    If successful, it prints "Row Updated" on console
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    column_to_update : string
        The column to be updated
    new_value : string
        The new value to be inserted in the column
    specific_id : string
        The ID of the employee whose row will be updated
    Returns None
    ------- 
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    query = f"UPDATE employees SET {column_to_update} =  %s WHERE employees.ID =  %s "
    try:
        # Execute the SQL query
        cursor.execute(query, (new_value, specific_id))
        # Commit the changes and close the connection
        connection.commit()
        connection.close()
    except mysql.connector.Error as error:
        print("An error occurred:", error)


def get_all_emp():
    """
    get_all_emp Desribtion :
    This function retrieves all the rows in the employees table in the database.
    If successful, it returns a pandas dataframe containing all the rows
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    None
    Returns
    -------
    employees_data : pandas dataframe
        A pandas dataframe containing all the rows in the employees table 
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    employees_data = pd.read_sql('SELECT * FROM employees', connection)
    # Close the cursor and connection
    cursor.close()
    connection.close()
    return employees_data

def get_emp(user_id):
    """
    get_emp Desribtion :
    This function retrieves a row in the employees table in the database.
    If successful, it returns a tuple containing the row
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    user_id : string
        The ID of the employee whose row will be retrieved
    Returns
    -------
    result : tuple
        A tuple containing the row in the employees table
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    # Your query goes here
    query = "SELECT employees.Name, employees.Department, employees.Position  FROM employees WHERE employees.ID =  %s"
    # Execute the query
    cursor.execute(query,(user_id,))
    # Fetch the result
    result = cursor.fetchone()
    # Store the columns in variables
    Name = result[0]
    Department = result[1]
    Position = result[2]
    # Close the cursor and connection
    cursor.close()
    connection.close()
    return (Name,Department,Position) 

def get_position(user_id):
    """
    get_position Desribtion :
    This function retrieves the position of an employee in the employees table in the database.
    If successful, it returns a string containing the position
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    user_id : string
        The ID of the employee whose position will be retrieved
    Returns
    -------
    position : string
        A string containing the position of the employee    
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    # Your query goes here
    query = "SELECT employees.Position  FROM employees WHERE employees.ID =  %s"
    # Execute the query
    cursor.execute(query,(user_id,))
    # Fetch the result
    result = cursor.fetchone()
    position = result[0]
    # Close the cursor and connection
    cursor.close()
    connection.close()
    return position

def group_by(user_id):
    """
    group_by Desribtion :
    This function retrieves the skills of an employee in the skills table in the database.
    If successful, it returns a tuple containing the skills
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    user_id : string
        The ID of the employee whose skills will be retrieved
    Returns
    -------
    result : tuple
        A tuple containing the skills of the employee
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    query = """ SELECT Skill_Type, GROUP_CONCAT(Skill_Name) AS skill_names
                FROM skills
                WHERE id = %s
                GROUP BY Skill_Type;"""
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()
    connection.close()
    return result

def get_all_skills():
    """
    get_all_skills Desribtion :
    This function retrieves all the rows in the skills table in the database.
    If successful, it returns a pandas dataframe containing all the rows
    If unsuccessful, it prints the error on console
    Parameters
    ----------
    None
    Returns
    -------
    skills_data : pandas dataframe
        A pandas dataframe containing all the rows in the skills table
    """
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)
    cursor = connection.cursor()
    skills_data = pd.read_sql('SELECT * FROM skills', connection)
    # Close the cursor and connection
    cursor.close()
    connection.close()
    return skills_data
