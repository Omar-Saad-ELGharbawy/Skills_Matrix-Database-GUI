import mysql.connector

host = 'localhost'
username = 'root'
password = '6@Monamo'
database = 'skills_matrix'

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




def insert_employee_row(user_data):
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)

    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO employees (ID, Name, Password, Department, Position)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query,user_data)
        connection.commit()

        connection.close()
        # print("EMP Inserted")
    except mysql.connector.Error as error:
        if error.errno == 1062:
            print("Duplicate entry error: This username already exists.")
    else:
        print("An error occurred:", error)


def update_emp(column_to_update,new_value,specific_id):
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)

    cursor = connection.cursor()
    # query = f"UPDATE {table_name} SET {column_to_update} = ? WHERE {id_column} = ?"

    # column_to_update = 'Name'
    # new_value = 'Omar'
    # specific_id = 'OmarSaad01'
    query = f"UPDATE employees SET {column_to_update} =  %s WHERE employees.ID =  %s "

#     # Execute the SQL query
    cursor.execute(query, (new_value, specific_id))
    # cursor.execute(query,)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()




def insert_skills_row(user_data):
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)

    cursor = connection.cursor()

    query = """
    INSERT INTO `skills` (`Skill_Name`,  `Skill_Type`, `ID`) 
    VALUES (%s, %s, %s)
    """

    cursor.execute(query,user_data)
    connection.commit()

    connection.close()
    # print("EMP Inserted")


def insert_skill(user_data):
    # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)

    cursor = connection.cursor()

    query = """
    INSERT INTO `skills` (`Skill_Name`,  `Skill_Type`, `ID`) 
    VALUES (%s, %s, %s)
    """

    cursor.execute(query,user_data)
    connection.commit()

    connection.close()
    # print("Skill Inserted")


def get_emp(user_id):

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

def group_by(user_id):

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


    
def perforom_Query(query):
        # Connect to the MySQL database
    connection = connect_to_database(host, username, password, database)

    cursor = connection.cursor()

    cursor.execute(query)
    connection.commit()

    connection.close()
    print("Done")



# result = group_by('Ahmed Galal01')
# print(result)

# print("Inser emp row")
# emp_data =  ('OmarSaad01', 'Omar Saad', "omar48", 'Embedded Software Engineering', 'Junior')
# insert_employee_row(emp_data)
# print("Inserted")

# skill_data = ('C', 'Languages', "OmarSaad01")
# insert_skills_row(skill_data)

# column_to_update = 'Name'
# new_value = 'Omar Saad'
# specific_id = 'OmarSaad01'

# column_to_update = 'Position'
# new_value = 'Senior'
# specific_id = 'OmarSaad01'
# update_emp(column_to_update,new_value,specific_id)

# query = "SELECT * FROM skills_matrix.employees;"
# perforom_Query(query)
userId = "Ahmed Galal01"
# (Name,Department,Position) =  get_emp(userId)
# # Output the values
# print("Column 1:", Name)
# print("Column 2:", Department)
# print("Column 3:", Position)

# skill_data=('Java', 'Languages', "OmarSaad01")
# insert_skill(skill_data)

# skills = group_by(userId)

# print(skills)