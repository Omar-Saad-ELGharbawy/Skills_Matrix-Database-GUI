import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='6@Monamo',
    database='my_skills_database'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Employees (ID VARCHAR(100),Name VARCHAR(300))")

print("Created")