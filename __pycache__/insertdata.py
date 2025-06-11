import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
val = ("Amit", 15, "10th")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

mydb.close()