import sqlite3

conn = sqlite3.connect("sqlite.db")
st_id = input("Enter the student id: ")
conn.execute("DELETE FROM student WHERE st_id = ?", (st_id,))
conn.commit()
conn.close()