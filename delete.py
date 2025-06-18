<<<<<<< HEAD
import sqlite3

conn = sqlite3.connect("sqlite.db")
st_id = input("Enter the student id: ")
conn.execute("DELETE FROM student WHERE st_id = ?", (st_id,))
conn.commit()
=======
import sqlite3

conn = sqlite3.connect("sqlite.db")
st_id = input("Enter the student id: ")
conn.execute("DELETE FROM student WHERE st_id = ?", (st_id,))
conn.commit()
>>>>>>> ab583f43d8413cdd27b4721a6660931f241fee07
conn.close()