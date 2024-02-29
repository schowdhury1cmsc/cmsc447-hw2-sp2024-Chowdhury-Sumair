import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

curs = connection.cursor()

# Adding test data to DB
curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Steve Smith', 211, 80))

curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Jian Wong', 122, 92))

curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Chris Peterson', 213, 91))

curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Sai Patel', 524, 94))

curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Andrew Whitehead', 425, 99))

curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Lynn Roberts', 626, 90))

curs.execute("INSERT INTO usrdata (username, id, points) VALUES (?, ?, ?)",
('Robert Sanders', 287, 75))

connection.commit()
connection.close()
