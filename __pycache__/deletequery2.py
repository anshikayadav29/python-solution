import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",     
    database="school"
)

cursor = mydb.cursor()

id = int(input("Enter student ID to delete: "))

query = "DELETE FROM students WHERE id = %s"
cursor.execute(query, (id,))

mydb.commit()

if cursor.rowcount > 0:
    print("Student deleted successfully.")
else:
    print("No student found with this ID.")

mydb.close()