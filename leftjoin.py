import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="school"
    )

    mycursor = mydb.cursor()

    print("{:<15} {:<20} {:<20}".format("State ID", "State Name", "Country ID"))

    sql = """
        SELECT state.state_id, state.state_name, country.country_id
        FROM state
        LEFT JOIN country
        ON state.country_id = country.country_id
    """

    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))

except:
    print("Error..")