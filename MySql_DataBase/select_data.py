import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='6@Monamo',
    database='my_skills_database'
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM employees"
# sql = "SELECT name FROM employees"
# sql = "SELECT name FROM employees WHERE name ='omar'"
# sql = "SELECT name FROM employees WHERE name like '%omar%' "
sql = "SELECT name FROM employees ORDER BY name"
sql = "SELECT name FROM employees ORDER BY name DESC"
sql = "SELECT name FROM employees LIMIT 2"
sql = "SELECT name FROM employees LIMIT 2 OFFSET 2"
mycursor.execute(sql)
# mycursor.execute(sql)

# # take data from user
# sql = "SELECT name FROM employees WHERE name= %s "
# data = ("omar",)
# mycursor.execute(sql,data)
# # result = mycursor.fetchone()

result = mycursor.fetchall()

for emp in result:
    print(emp)

print("Selected")

