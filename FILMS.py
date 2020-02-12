import sqlite3

con = sqlite3.connect("Films.db")
curs = con.cursor()

curs.execute("""CREATE TABLE Films  
                  (id INTEGER PRIMARY KEY, 
                  Title TEXT, 
                  Notes TEXT, 
                  Genre TEXT,
                  Realize INTEGER,
                  FOREIGN KEY (Notes) REFERENCES Books(Based_on),
                  FOREIGN KEY (realize) REFERENCES Realize(Realize_year))""")

curs.execute("""CREATE TABLE Realize
                  (id INTEGER PRIMARY KEY,
                  Director TEXT,
                  RT INTEGER,
                  Realize_year INTEGER)
                  """)

curs.execute("""CREATE TABLE Books
                  (id INTEGER PRIMARY KEY,
                  Distributor TEXT,
                  Based_on TEXT,
                  Author TEXT)
                  """)

curs.execute('INSERT INTO Films (Title, Notes , Genre , Realize) '
             'VALUES ("	Carrie", "Based on the novel of the same name", "Mystic", "1976")')
curs.execute('INSERT INTO Films (Title, Notes , Genre , Realize) '
             'VALUES ("	The Shining", "Based on the novel of the same name", "Horrors", "1980")')
curs.execute('INSERT INTO Films (Title, Notes , Genre , Realize) '
             'VALUES ("	Silver Bullet", "Based on the novel Cycle of the Werewolf.", "Gothic", "1985")')

curs.execute('INSERT INTO Realize (Director, RT, Realize_year) '
             'VALUES ("	Brian De Palma", "92", "1976")')
curs.execute('INSERT INTO Realize (Director, RT, Realize_year) '
             'VALUES ("Stanley Kubrick", "85", "1980")')
curs.execute('INSERT INTO Realize (Director, RT, Realize_year) '
             'VALUES ("	Dan Attias", "47", "1985")')

curs.execute('INSERT INTO Books( Distributor , Based_on, Author) '
             'VALUES ("United Artists", "Book", "Stephen King")')
curs.execute('INSERT INTO Books( Distributor , Based_on, Author) '
             'VALUES ("	Warner Bros.", "Book", "Stephen King")')
curs.execute('INSERT INTO Books( Distributor , Based_on, Author) '
             'VALUES ("Paramount Pictures", "Book", "Stephen King")')
con.commit()

curs.close()
con.close()