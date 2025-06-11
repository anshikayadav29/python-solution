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

    
    sql = "SELECT * FROM student ORDER BY st_name ASC LIMIT 3"
    cursor.execute(sql)

    results = cursor.fetchall()

    for row in results:
        print("{:<5} {:<20} {:<10} {:<25}".format(row[0], row[1], row[2], row[3]))

except Exception as e:
    print("Error:", e)

finally:
    mydb.close()