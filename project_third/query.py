import sqlite3
# Create a SQL connection to our SQLite database
con = sqlite3.connect("bookdatabase.db")

cur = con.cursor()

# Return all
# Return first result of query
for row in cur.execute('SELECT * FROM note WHERE id="abc"'):
    print (row)

cur.fetchall()
# cur.fetchall()

# Be sure to close the connection
con.close()