import sqlite3


with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies WHERE Title = 'Terminator'"
    cursor = conn.execute(command)
    # This method get data into a cursor object which is able to iter many times so that it can print it out each
    for row in cursor:
        Title = str(row)

print(Title)
