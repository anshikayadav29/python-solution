import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
    )

def insert():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    db.commit()
    print("Record inserted")
    db.close()

def display():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    db.close()

def update():
    student_id = int(input("Enter student ID to update: "))
    new_name = input("Enter new name: ")
    db = connect()
    cursor = db.cursor()
    cursor.execute("UPDATE students SET name = %s WHERE id = %s", (new_name, student_id))
    db.commit()
    print("Record updated")
    db.close()

def delete():
    student_id = int(input("Enter student ID to delete: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    db.commit()
    print("Record deleted")
    db.close()

while True:
    print("\n1. Insert\n2. Display\n3. Update\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        insert()
    elif choice == '2':
        display()
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        break
    else:
        print("Invalid choice")