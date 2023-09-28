import mysql.connector
from database_connection import *

""" database_init File Documentation :
This file contains functions to create the database if not created and the tables
It also contains a function to establish a connection to the database
Functions :
    check_database_exists(host, username, password, database)
    create_database(host, username, password, database)
    create_employees_table()
    create_skills_table()
"""

def check_database_exists(host, username, password, database):
    """ check_database_exists Desribtion :
    This function checks if the database exists
    If the database exists, it returns True
    If the database does not exist, it returns False
    """
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        # Database exists
        exists = True
        # Close the connection
        connection.close()
    except mysql.connector.Error as error:
        # Database does not exist
        exists = False
    return exists

def create_database(host, username, password, database):
    """
    create_database Desribtion:
    This function creates the database
    If successful, it prints "Database Created" on console
    If unsuccessful, an exception is raised
    """
    mydb = mysql.connector.connect(
    host=host,
    user=username,
    passwd=password)
    cursor = mydb.cursor()
    sql ="CREATE DATABASE "+database
    cursor.execute(sql)
    mydb.close()
    print("Created")

# Function to create the "employees" table
def create_employees_table():
    """
    create_employees_table Desribtion:
    This function creates the "employees" table
    If successful, it prints "Table "employees" created successfully" on console
    If unsuccessful, it prints "Failed to create table "employees"" on console
    and raises an Exception
    """
    mydb = connect_to_database(host, username, password, database)
    cursor = mydb.cursor()
    sql = '''
    DROP TABLE IF EXISTS employees;
    CREATE TABLE employees (
        ID VARCHAR(16) NOT NULL,
        Name TEXT NOT NULL,
        Password VARCHAR(16) NOT NULL,
        Department TEXT NOT NULL,
        Position TEXT NOT NULL,
        PRIMARY KEY (ID),
        KEY ID (ID),
        KEY ID_2 (ID)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    '''
    cursor.execute(sql)
    mydb.close()
    print('Table "employees" created successfully')

# Function to create the "skills" table
def create_skills_table():
    """
    create_skills_table Desribtion:
    This function creates the "skills" table
    If successful, it prints "Table "skills" created successfully" on console
    If unsuccessful, it prints "Failed to create table "skills"" on console
    and raises an Exception
    """

    mydb = connect_to_database(host, username, password, database)
    cursor = mydb.cursor()
    sql = '''
    DROP TABLE IF EXISTS skills;
    CREATE TABLE skills (
        Skill_ID INT(10) AUTO_INCREMENT,
        Skill_Name TEXT NOT NULL,
        Skill_Type TEXT NOT NULL,
        ID VARCHAR(16) NOT NULL,
        PRIMARY KEY (Skill_ID),
        KEY ID (ID),
        CONSTRAINT skills_ibfk_1 FOREIGN KEY (ID) REFERENCES employees (ID)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    '''
    cursor.execute(sql)
    mydb.close()
    print('Table "skills" created successfully')



# ############################################## Main #########################################

# help(check_database_exists)
if(check_database_exists(host, username, password, database)):
    print("Database exists")
else:
    print("Database does not exist")
    create_database(host, username, password, database)
    print(f"{database} Database Created")

# Create the tables
create_employees_table()
print("Employees Created")
create_skills_table()
print("Skills Created")
