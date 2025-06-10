import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="school"
    )

    cursor = mydb.cursor()

    print("{:<5} {:<20} {:<10} {:<25}".format("ID", "Name", "Class", "Email"))

    name = input("Enter the Student Name (or part of it): ")

    sql = "SELECT * FROM student WHERE st_name LIKE %s"
    val = ("%" + name + "%",)
    cursor.execute(sql, val)

    results = cursor.fetchall()

    if results:
        for row in results:
            print("{:<5} {:<20} {:<10} {:<25}".format(row[0], row[1], row[2], row[3]))
    else:
        print("No student found with that name.")

except Exception as e:
    print("Error:", e)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()