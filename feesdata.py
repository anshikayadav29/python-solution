import sqlite3


conn = sqlite3.connect("sqlite.db")
cur = conn.cursor()

# Create fees table (if not exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS fees (
    st_id INTEGER,
    fees INTEGER
)
""")
cur.execute("SELECT COUNT(*) FROM fees")
if cur.fetchone()[0] == 0:
    cur.executemany("INSERT INTO fees (st_id, fees) VALUES (?, ?)", [
        (1, 2000),
        (2, 2500),
        (3, 1800),
        (4, 3000),
        (5, 2100),
        (6, 2200)
    ])
    conn.commit()


for row in cur.execute("""
SELECT student.st_id, student.st_name, fees.fees
FROM student
JOIN fees ON student.st_id = fees.st_id
"""):
    print(row)

conn.close()