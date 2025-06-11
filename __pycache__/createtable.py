import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",   
    database="school"
)

print("Connection successful!")

mydb.close()