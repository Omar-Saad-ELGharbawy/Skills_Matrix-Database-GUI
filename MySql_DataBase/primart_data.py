# import mysql.connector

# # Establish a connection to the MySQL server
# conn = mysql.connector.connect(
#     host="localhost",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

# # Create a cursor object to execute SQL queries
# cursor = conn.cursor()

# # Define the SQL query to create a table
# create_table_query = """
# CREATE TABLE my_table (
#     id INT AUTO_INCREMENT,
#     name VARCHAR(50),
#     age INT,
#     PRIMARY KEY (id)
# )
# """

# # Execute the SQL query to create the table
# cursor.execute(create_table_query)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()




###########################################################


# import mysql.connector

# # Establish a connection to the MySQL server
# conn = mysql.connector.connect(
#     host="localhost",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

# # Create a cursor object to execute SQL queries
# cursor = conn.cursor()

# # Define the SQL query to insert a row into the table
# insert_query = """
# INSERT INTO my_table (name, age)
# VALUES (%s, %s)
# """

# # Define the values to insert
# name = "John"
# age = 25
# values = (name, age)

# # Execute the SQL query to insert the row
# cursor.execute(insert_query, values)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()