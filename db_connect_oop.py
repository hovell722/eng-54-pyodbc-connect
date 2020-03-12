import pyodbc

class MSDBConnection():
    # We need to connect to our database

    def __init__(self):
        # Variables for connections
        self.database = 'Northwind'
        self.username = 'SA'
        self.passwords = 'Passw0rd2018'
        # make connection
        self.conn = pyodbc.connect('DSN=MYMSSQL;UID=' + self.username + ';PWD=' + self.passwords + ';' + 'DATABASE=' + self.database)
        # making cursor
        self.cursor = self.conn.cursor()





nw_db_object = MSDBConnection()

rows = nw_db_object.sql_query('SELECT * FROM Products')

print(rows.fetchone())

