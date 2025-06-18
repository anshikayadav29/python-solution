import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")
print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
seen = set() 
for n in data:
    if n[1] not in seen:  
        print(n[0], n[1], n[2], n[3])  
        seen.add(n[1])  
