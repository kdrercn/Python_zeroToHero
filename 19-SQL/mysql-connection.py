import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "node-app"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")


