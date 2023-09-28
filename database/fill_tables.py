import mysql.connector

host = 'localhost'
username = 'root'
password = '6@Monamo'
database = 'skills_matrix_database'

""" fill_tables File Documentation :
This file contains functions to insert data into the database
Functions :
    connect_to_database(host, username, password, database)
    insert_data_to_employees(data_list)
    insert_data_to_skills(data_list)
"""

# Function to establish a database connection
def connect_to_database(host, username, password, database):
    mydb = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    if mydb.is_connected():
        print('Connected to the database')
    else:
        print('Failed to connect to the database')
    return mydb


def insert_data_to_employees(data_list):
    """
    insert_data_to_employees Desribtion:
    This function inserts data into the employees table
    If successful, it prints "Employees Inserted" on console
    If unsuccessful, an exception is raised
    Parameters:
        data_list (list): list of tuples containing the data to be inserted
    Returns:
        None
    """
    mydb = connect_to_database(host, username, password, database)
    cursor = mydb.cursor()
    sql = """
    INSERT INTO employees (ID, Name, Password, Department, Position)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.executemany(sql, data_list)
    mydb.commit()
    mydb.close()

def insert_data_to_skills(data_list):
    """
    insert_data_to_skills Desribtion:
    This function inserts data into the skills table
    If successful, it prints "Skills Inserted" on console
    If unsuccessful, an exception is raised
    Parameters:
        data_list (list): list of tuples containing the data to be inserted
    Returns:
        None
    """
    mydb = connect_to_database(host, username, password, database)
    cursor = mydb.cursor()
    sql = """
    INSERT INTO `skills` (`Skill_Name`,  `Skill_Type`, `ID`) 
    VALUES (%s, %s, %s)
    """
    cursor.executemany(sql, data_list)
    mydb.commit()
    mydb.close()

# ###############################################################################################


# Define employees data to be inserted
emp_data = [
    ('UserId1', 'UserName1', 'UserPassword1', 'UserDepartment1', 'UserPosition1'),
    ('UserId2', 'UserName2', 'UserPassword2', 'UserDepartment2', 'UserPosition2'),
    ('UserId3', 'UserName3', 'UserPassword3', 'UserDepartment3', 'UserPosition3'),
    ('UserId4', 'UserName4', 'UserPassword4', 'UserDepartment4', 'UserPosition4'),
    ('AdminID', 'AdminName', 'AdminPassword', 'AdminDepartment', 'Admin'),
]

# Define skills data to be inserted
skills_data = [
    ('Leadership', 'Soft skills', 'UserId1'),
    ('Python', 'Programming Languages', 'UserId1'),
    ('C', 'Programming Languages', 'UserId1'),
    ('C++', 'Programming Languages', 'UserId1'),
    ('Arabic', 'Languages', 'UserId1'),
    ('English', 'Languages', 'UserId1'),
    ('Software Development', 'Technical Skills', 'UserId1'),
    ('Leadership', 'Soft Skills', 'UserId2'),
    ('C', 'Programming Languages', 'UserId2'),
    ('Leadership', 'Technical Skills', 'AdminID'),
]

# Call the function to insert the data
insert_data_to_employees(emp_data)
print("Employees Inserted")
insert_data_to_skills(skills_data)
print("SKills Inserted")

