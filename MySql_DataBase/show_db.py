import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='6@Monamo')

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)

print("Showed")