import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='6@Monamo',
    database='my_skills_database'
)

mycursor = mydb.cursor()

sql = "INSERT INTO employees(ID,Name) VALUE(%s , %s)"

# data = ("01","Omar")
# mycursor.execute(sql,data)

# many_data=[
#     ("02","Ahmed"),
#     ("03","Osama")
# ]

many_data=[
    ("04","Nardine"),
    ("05","Maisara")
]
mycursor.executemany(sql,many_data)

mydb.commit()

print("Inserted")

print(mycursor.lastrowid)