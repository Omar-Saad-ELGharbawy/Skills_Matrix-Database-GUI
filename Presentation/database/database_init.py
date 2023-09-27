
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
database = 'skills_matrix'

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

    mydb.close()

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
    
    # return mydb

# Function to create the "employees" table
def create_employees_table():

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


def insert_data_to_employees(data_list):

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

    mydb = connect_to_database(host, username, password, database)

    cursor = mydb.cursor()
    sql = """
    INSERT INTO `skills` (`Skill_Name`,  `Skill_Type`, `ID`) 
    VALUES (%s, %s, %s)
    """
    cursor.executemany(sql, data_list)

    mydb.commit()
    mydb.close()


# Main function to execute the SQL code
def execute_sql():
    if(check_database_exists(host, username, password, database)):
        print("Database exists")
    else:
        print("Database does not exist")
        create_database(host, username, password, database)
        print("Database Created")

    # mydb = connect_to_database(host, username, password, database)
    # print("Connected")

    # Create the tables
    create_employees_table()
    print("Employees Created")
    create_skills_table()
    print("Skills Created")
    




# ############################################## Main #########################################
# Call the main function to execute the SQL code
# execute_sql()

# Define the data to be inserted
emp_data = [
    ('Engy01', 'Engy', '100', 'Integration', 'Technical Manager'),
    ('Ahmed Galal01','Ahmed Galal', '200',  'Integration', 'Team leader'),
    ('Mohamed Tarek', 'Mohamed Tarek', '101', 'Embedded Software Engineering', 'Team Leader '),
    ('Ahmed Shindy01','Ahmed Shindy',"301", 'Embedded Software Engineering', 'Junior Engineer'),
    ('Assem01','Assem', '102', 'Embedded Software Engineering', 'Junior Engineer'),
    ('Abdeen01','Abdeen', '203', 'Algo', 'Team Leader'),
    ('Amr01','Amr', '102', 'Algo', 'Junior')
]

skills_data = [
    ('Leadership', 'Soft skills', "Engy01"),
    ('Python', 'Languages', 'Ahmed Galal01'),
    ('C', 'Languages', 'Ahmed Galal01'),
    ('C++', 'Languages', 'Ahmed Galal01'),
    ('Software Development', 'Technical Skills', 'Ahmed Galal01'),
    ('Leadership', 'Soft Skills', 'Ahmed Galal01'),
    ('C_Programming', 'Languages', 'Assem01'),
    ('ARM Interfacing', 'Technical Skills', 'Assem01'),
    ('Problem Solving', 'Soft Skills', 'Assem01'),
    ('ARM_Interfacing', 'Technical Skills', 'Ahmed Shindy01'),
    ('Embedded Linux', 'Technical Skills', 'Ahmed Shindy01'),
    ('Machine Learning and AI', 'Technical Skills', 'Abdeen01'),
    ('Automotive Engineering', 'Technical Skills', 'Mohamed Tarek'),
    ('AUTOSAR', 'Technical Skills', 'Mohamed Tarek'),
    ('LeaderShip', 'Soft Skills', 'Mohamed Tarek'),
    ('Computer Vision', 'Technical Skills', 'Amr01'),
    ('Problem Solving', 'Soft Skills', 'Amr01'),
    ('Machine Learning', 'Technical Skills', 'Amr01'),
]

# # # Call the function to insert the data

# insert_data_to_employees(emp_data)
# insert_data_to_skills(skills_data)
# print("Inserted")

