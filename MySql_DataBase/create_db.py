import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='6@Monamo')

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE my_skills_database")

print("Created")