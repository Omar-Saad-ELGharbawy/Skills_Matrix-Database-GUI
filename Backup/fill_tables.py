# from database_init import connect_to_database , host, username , password, database

import mysql.connector

host = 'localhost'
username = 'root'
password = '6@Monamo'
database = 'new_skills_matrix'
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




# Define the data to be inserted
emp_data = [
    # ('Engy01', 'Engy', '100', 'Integration', 'Technical Manager'),
    # ('Ahmed Galal01','Ahmed Galal', '200',  'Integration', 'Team leader'),
    # ('Mohamed Tarek', 'Mohamed Tarek', '101', 'Embedded Software Engineering', 'Team Leader '),
    # ('Ahmed Shindy01','Ahmed Shindy',"301", 'Embedded Software Engineering', 'Junior Engineer'),
    ('Assem01','Assem', '102', 'Embedded Software Engineering', 'Junior Engineer'),
    ('Abdeen01','Abdeen', '203', 'Algo', 'Team Leader'),
    # ('Amr01','Amr', '102', 'Algo', 'Junior')
]

skills_data = [
    # ('Leadership', 'Soft skills', "Engy01"),
    # ('Python', 'Languages', 'Ahmed Galal01'),
    # ('C', 'Languages', 'Ahmed Galal01'),
    ('C++', 'Languages', 'Ahmed Galal01'),
    ('Software Development', 'Technical Skills', 'Ahmed Galal01'),
    ('Leadership', 'Soft Skills', 'Ahmed Galal01'),
    # ('C_Programming', 'Languages', 'Assem01'),
    # ('ARM Interfacing', 'Technical Skills', 'Assem01'),
    # ('Problem Solving', 'Soft Skills', 'Assem01'),
    # ('ARM_Interfacing', 'Technical Skills', 'Ahmed Shindy01'),
    # ('Embedded Linux', 'Technical Skills', 'Ahmed Shindy01'),
    # ('Machine Learning and AI', 'Technical Skills', 'Abdeen01'),
    # ('Automotive Engineering', 'Technical Skills', 'Mohamed Tarek'),
    # ('AUTOSAR', 'Technical Skills', 'Mohamed Tarek'),
    # ('LeaderShip', 'Soft Skills', 'Mohamed Tarek'),
    # ('Computer Vision', 'Technical Skills', 'Amr01'),
    # ('Problem Solving', 'Soft Skills', 'Amr01'),
    # ('Machine Learning', 'Technical Skills', 'Amr01'),
]

# # # Call the function to insert the data

insert_data_to_employees(emp_data)
print("Employees Inserted")
insert_data_to_skills(skills_data)
print("SKills Inserted")

