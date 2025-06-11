import pymysql

# MySQL se connection
db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="school"
)

mycursor = db.cursor()

print("{:<15}".format("Order Amount"))

try:
    sql = "SELECT order_amount FROM orders"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))
except:
    print("Error..")