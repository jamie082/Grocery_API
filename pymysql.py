import sqlite3

# Create a SQL connection to our SQLlite database
con = sqlite3 = sqlite3.connect("bookdatabase.db")

cur = con.cursor()

# The result of our "cursor.execute" can be interated over by a row
for row in cur.execute("SELECT * FROM note;"):
    print(row)

con.close()