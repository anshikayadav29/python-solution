import sqlite3

conn = sqlite3.connect("sqlite.db")
print("STUDENT ID | STUDENT NAME | STUDENT FEES")

data = conn.execute("""
SELECT student.st_id, student.st_name, fees.fees
FROM student
JOIN fees ON student.st_id = fees.st_id
""")

for a in data:
    print(a)

conn.close()