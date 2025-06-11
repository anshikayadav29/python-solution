import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="school"
)

cursor = mydb.cursor()


name = input("Enter the updated Student Name: ")
class_name = input("Enter the updated Class: ")
email = input("Enter the updated Email: ")
student_id = int(input("Enter the Student ID to update: "))


query = "UPDATE student SET st_name = %s, st_class = %s, st_email = %s WHERE id = %s"
data = (name, class_name, email, student_id)

try:
    cursor.execute(query, data)
    mydb.commit()
    if cursor.rowcount > 0:
        print("Student data updated successfully.")
    else:
        print("No student found with this ID.")
except Exception as e:
    print("Error while updating:", e)

mydb.close()