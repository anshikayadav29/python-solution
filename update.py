<<<<<<< HEAD
import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
      update student set st_name='ravi',st_class='10th'where st_id=1




''')
conn.commit()
=======
import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
      update student set st_name='ravi',st_class='10th'where st_id=1




''')
conn.commit()
>>>>>>> ab583f43d8413cdd27b4721a6660931f241fee07
conn.close()