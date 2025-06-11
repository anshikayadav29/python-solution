import pymysql as mq

try:
    
    conn = mq.connect(host="localhost", user="root", password="1234", database="school")
    cur = conn.cursor()

    print("{:<15}".format("Order Avg"))

    
    sql = "SELECT AVG(order_amount) FROM orders"
    cur.execute(sql)

    sdata = cur.fetchall()

    for a in sdata:
        print("{:<15}".format(a[0]))

except Exception as e:
    print("Error:", e)

finally:
    conn.close()