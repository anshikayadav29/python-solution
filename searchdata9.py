import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")
print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
seen = set() 
for n in data:
    if n[1] not in seen:  
        print(n[0], n[1], n[2], n[3])  
        seen.add(n[1])  


st_name=input("Enter the student Name:- ")
st_class=input("Enter the class Nmae:- ")

data=conn.execute("SELECT*FROM student where st_name like '%"+st_name+"%' or st_class='"+st_class+"'  ")
for n in data:
    print(n[0],"  ",n[1],"   ",n[2],n[3])