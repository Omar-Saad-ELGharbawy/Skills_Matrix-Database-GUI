
# mydb = mysql.connector.connect(
#     host="localhost",
#     user='root',
#     passwd='6@Monamo',
#     database='my_skills_database'
# )

import mysql.connector

host = 'localhost'
username = 'root'
password = '6@Monamo'
database = 'skills_database'

def check_database_exists(host, username, password, database):
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
    mydb = mysql.connector.connect(
    host=host,
    user=username,
    passwd=password)

    cursor = mydb.cursor()
    sql ="CREATE DATABASE "+database
    print(sql)
    cursor.execute(sql)

    print("Created")

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

# Function to create the "employees" table
def create_employees_table(mydb):
    cursor = mydb.cursor()

    sql = '''
    DROP TABLE IF EXISTS employees;
    CREATE TABLE employees (
        Name TEXT NOT NULL,
        Password VARCHAR(16) NOT NULL,
        ID INT(11) NOT NULL,
        Department TEXT NOT NULL,
        Position TEXT NOT NULL,
        PRIMARY KEY (ID),
        KEY ID (ID),
        KEY ID_2 (ID)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    '''
    cursor.execute(sql)
    print('Table "employees" created successfully')

# Function to create the "skills" table
def create_skills_table(mydb):
    cursor = mydb.cursor()

    sql = '''
    DROP TABLE IF EXISTS skills;
    CREATE TABLE skills (
        Skill_Name TEXT NOT NULL,
        Skill_ID INT(10) NOT NULL,
        Skill_Type TEXT NOT NULL,
        ID INT(11) NOT NULL,
        PRIMARY KEY (Skill_ID),
        KEY ID (ID),
        CONSTRAINT skills_ibfk_1 FOREIGN KEY (ID) REFERENCES employees (ID)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
    '''
    cursor.execute(sql)
    print('Table "skills" created successfully')

# Main function to execute the SQL code
def execute_sql():
    if(check_database_exists(host, username, password, database)):
        print("Database exists")
    else:
        print("Database does not exist")
        create_database(host, username, password, database)

    mydb = connect_to_database(host, username, password, database)
    print("Connected")

    # Create the tables
    # create_employees_table(mydb)
    create_skills_table(mydb)

    # Close the database connection
    return mydb
    

def insert_data_to_employees(mydb,data_list):

    cursor = mydb.cursor()
    sql = """
    INSERT INTO employees (Name, Password, ID, Department, Position)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.executemany(sql, data_list)

    mydb.commit()

def insert_data_to_skills(mydb,data_list):

    cursor = mydb.cursor()
    sql = """
    INSERT INTO `skills` (`Skill_Name`, `Skill_ID`, `Skill_Type`, `ID`) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(sql, data_list)

    mydb.commit()



# ############################################## Main #########################################
# Call the main function to execute the SQL code
# mydb = execute_sql()

mydb = connect_to_database(host, username, password, database)


# Define the data to be inserted
# emp_data = [
#     ('Engy', '100', 1, 'Integration', 'Technical Manager'),
#     ('Ahmed Galal', '200', 2, 'Integration', 'Team leader')
# ]

emp_data = [
    # ('Engy', '100', 1, 'Integration', 'Technical Manager'),
    # ('Ahmed Galal', '200', 2, 'Integration', 'Team leader'),
    ('Mohamed Tarek', '101', 101, 'Embedded Software Engineering', 'Team Leader '),
    ('Ahmed Shindy', '301', 103, 'Embedded Software Engineering', 'Junior Engineer'),
    ('Ahmed Shindy', '', 104, 'Embedded Software Engineering', 'Junior Engineer'),
    ('Abdulrahman Assem', '102', 201, 'Embedded Software Engineering', 'Junior Engineer'),
    ('Abdeen', '203', 302, 'Algo', 'Team Leader'),
    ('Amr', '102', 2011, 'Algo', 'Junior')
]

# skills_data = [
#     ('Leadership', 1, 'Soft skills', 1),
#     ('Python', 2, 'Technical skills', 2)
# ]
skills_data = [
    # ('Leadership', 1, 'Soft skills', 1),
    # ('Python', 2, 'Technical skills', 2),
    # ('C_Programming', 3, 'Technical skills', 201),
    ('ARM_Interfacing', 4, 'Technical Skills', 103),
    ('Embedded Linux', 5, 'Technical Skills', 103),
    ('Machine Learning and AI', 6, 'Technical Skills', 302),
    ('Automotive Engineering', 7, 'Technical Skills', 101),
    ('LeaderShip', 9, 'Soft Skills', 101),
    ('Computer Vision', 10, 'Technical Skills', 2011),
    ('Problem Solving', 11, 'Soft Skills', 2011),
    ('ARM Interfacing', 12, 'Technical Skills', 201),
    ('Problem Solving', 13, 'Soft Skills', 201),
    ('Leadership', 14, 'Soft Skills', 2),
    ('C\\C++ Software Development', 15, 'Technical Skills', 2),
    ('Machine Learning', 16, 'Technical Skills', 2011),
    ('AUTOSAR', 18, 'Technical Skills', 101)
]

# Call the function to insert the data
# insert_data_to_employees(mydb,emp_data)
insert_data_to_skills(mydb,skills_data)

print("Inserted")