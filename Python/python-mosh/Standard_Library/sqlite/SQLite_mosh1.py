import sqlite3
import json
from pathlib import Path


# read data from database
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # This method get data into a cursor object which is able to iter many times so that it can print it out each
    for row in cursor:
        print(row)
    # This method fetch all the object in database into a list
    movies = cursor.fetchall()
    print(movies)
