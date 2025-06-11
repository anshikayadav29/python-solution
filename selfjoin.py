import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="school"
    )

    cur = db.cursor()

    sql = """
    SELECT c1.category_name, c2.category_name 
    FROM categories AS c1 
    JOIN categories AS c2 ON c1.parent_id = c2.category_id
    """

    cur.execute(sql)
    sdata = cur.fetchall()

    for a in sdata:
        print(a)

except Exception as e:
    print("Error:", e)