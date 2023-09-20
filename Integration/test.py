import mysql.connector

host = 'localhost'
username = 'root'
password = '6@Monamo'
database = 'skills_database'

def group_by(user_id):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    # Query to check if the user_id and password exist in the database
    # query = """SELECT Skill_Name, Skill_Type,ID
    #         FROM skills
    #         GROUP BY Skill_Type
    #         HAVING ID = %s"""
    # query = "SELECT * FROM skills"
    query = """ SELECT Skill_Type, GROUP_CONCAT(Skill_Name) AS skill_names
                FROM skills
                WHERE id = %s
                GROUP BY Skill_Type;"""

    cursor.execute(query, (user_id,))

    result = cursor.fetchall()
    connection.close()
    return result

result = group_by(1)

print(result)