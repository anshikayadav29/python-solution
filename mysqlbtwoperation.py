import mysql.connector as mq

try:
    conn = mq.connect(
        host="localhost",
        user="root",
        password="1234",     
        database="school"
    )

    mycursor = conn.cursor()

    print("{:<15} {:<20}".format("State Id", "State Name"))

    sql = "SELECT state_id, state_name FROM state"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15} {:<20}".format(s[0], s[1]))

except Exception as e:
    print("Error:", e)

finally:
    if 'conn' in locals():
        conn.close()