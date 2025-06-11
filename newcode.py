import mysql.connector


host = "localhost"
user = "root"
password = ""  

try:
    
    mydb = mysql.connector.connect(
        host=host,
        user=user,
:    )

    cursor = mydb.cursor()

    
    cursor.execute("CREATE DATABASE school")
    print("Database created successfully!")

except mysql.connector.Error as err:
    print(f"Database error: {err}")