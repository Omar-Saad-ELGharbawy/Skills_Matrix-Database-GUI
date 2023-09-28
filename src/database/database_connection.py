import mysql.connector

"""
This module is used to connect with the database and execute queries on it,
It contains the main Database Parameters:
    host
    username
    password
    database
    and a function that connects to the DB using those parameters
"""

host = 'localhost'
username = 'root'
password = '6@Monamo'
# database = 'skills_matrix_database'
database = 'new_table'

# Function to establish a database connection
def connect_to_database(host, username, password, database):
    """
    connect_to_database Desribtion:
    This function establishes a connection to the database
    If successful, it returns the connection object and closes it after use
    If unsuccessful, it prints "Failed to connect to the database" on console
    and raises an Exception
    """
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

