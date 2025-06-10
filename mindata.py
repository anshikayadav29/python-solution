import pymysql as mq

try:
    conn = mq.connect(host="localhost", user="root", password="1234", database="school")
    mycursor = conn.cursor()

    mycursor.execute("SELECT MAX(order_amount) FROM orders")
    max_amt = mycursor.fetchone()[0]

    mycursor.execute("SELECT MIN(order_amount) FROM orders")
    min_amt = mycursor.fetchone()[0]

    print("Maximum Order Amount:", max_amt)
    print("Minimum Order Amount:", min_amt)

except Exception as e:
    print("Error:", e)

finally:
    conn.close()