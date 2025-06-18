<<<<<<< HEAD
import sqlite3

conn = sqlite3.connect("sqlite.db")

ins1 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('ravi', '12th', 'ravi@gmail.com')"
ins2 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('ram', '11th', 'ram@gmail.com')"
ins3 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('naincy', '12th', 'naincy@gmail.com')"
ins4 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('muskan', '12th', 'muskan@gmail.com')"
ins5 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('khushi', '12th', 'khushi@gmail.com')"
ins6 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('shreya', '12th', 'shreya@gmail.com')"
ins7 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('bhanu', '12th', 'bhanu@gmail.com')"

conn.execute(ins1)
conn.execute(ins2)
conn.execute(ins3)
conn.execute(ins4)
conn.execute(ins5)
conn.execute(ins6)
conn.execute(ins7)

conn.commit()
=======
import sqlite3

conn = sqlite3.connect("sqlite.db")

ins1 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('ravi', '12th', 'ravi@gmail.com')"
ins2 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('ram', '11th', 'ram@gmail.com')"
ins3 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('naincy', '12th', 'naincy@gmail.com')"
ins4 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('muskan', '12th', 'muskan@gmail.com')"
ins5 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('khushi', '12th', 'khushi@gmail.com')"
ins6 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('shreya', '12th', 'shreya@gmail.com')"
ins7 = "INSERT OR IGNORE INTO student(st_name, st_class, st_email) VALUES ('bhanu', '12th', 'bhanu@gmail.com')"

conn.execute(ins1)
conn.execute(ins2)
conn.execute(ins3)
conn.execute(ins4)
conn.execute(ins5)
conn.execute(ins6)
conn.execute(ins7)

conn.commit()
>>>>>>> ab583f43d8413cdd27b4721a6660931f241fee07
conn.close()