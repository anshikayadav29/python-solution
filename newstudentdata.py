import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="school"
)

cursor = mydb.cursor()


students = [
    ("Aman", "10th", "aman@gmail.com"),
    ("Riya", "11th", "riya@gmail.com"),
    ("Karan", "12th", "karan@gmail.com"),
    ("Neha", "9th", "neha@gmail.com"),
    ("Mohit", "10th", "mohit@gmail.com"),
    ("Sana", "8th", "sana@gmail.com")
]

query = "INSERT INTO student (st_name, st_class, st_email) VALUES (%s, %s, %s)"

cursor.executemany(query, students)

mydb.commit()
print("6 students inserted successfully!")

mydb.close()