import pymysql as mq


mydb = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor = mydb.cursor()

try:
    
    ins = "INSERT INTO student (st_name, st_class, st_email) VALUES (%s, %s, %s)"
    
    
    t = ("ram", "12th", "ram@gmail.com")
    
    
    mycursor.execute(ins, t)
    
    
    mydb.commit()
    
    print("Insert Data")
    
except Exception as e:
    print("Error:", e)