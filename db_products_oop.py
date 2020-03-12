from db_connect_oop import *

class NWProducts(MSDBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Products'

    def __sql_query(self, query): # private to avoid SQL injection
        return self.cursor.execute(query)

    def __filter_sql_injection(self, query):
        # do some regular expression to filter sql attacks
        # return
        pass

    # Write all the CRUD methods

    # R - Read ONE product based on id (select)

    # Read ALL products (select)

    def read_all(self):
        # return data with all products
        rows = self.__sql_query(f'SELECT * FROM {self.table}')
        return rows

    # Create ONE products (insert)
    # tip: search commit for pyodbc

    # delete (delete)