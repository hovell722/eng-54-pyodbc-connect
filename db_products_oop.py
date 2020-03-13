from db_connect_oop import *

class NWProducts(MSDBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Products'

    def __sql_query(self, query):  # private to avoid user SQL injection
        return self.cursor.execute(query)

    def read_all(self):
        # return data with all products
        rows = self.__sql_query(f'SELECT * FROM {self.table}')
        return rows

    # READ ALL products (select)

    # Write all the CRUD methods

    def read_one(self, product_id):
        row = self.__sql_query(f'SELECT * FROM {self.table} WHERE ProductID = {product_id}')
        return row
    # R - Read ONE product based on id :) (Select)

    def create_one(self, product_name, supplier_id, category_id, quantity, price, stock, order, reorder, discontinued):
        self.__sql_query(f"INSERT INTO {self.table} (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)" +
        f" VALUES ('{product_name}', {supplier_id}, {category_id}, '{quantity}', {price}, {stock}, {order}, {reorder}, {discontinued})")
        self.conn.commit()

    # Create ONE product (insert)
    # tip: search commit for pyodb

    def delete_one(self, product_id):
        self.__sql_query(f"DELETE FROM {self.table} WHERE ProductID = {product_id}")
        self.conn.commit()

    # delete (delete)

    # def __filter_sql_injection(self, query):

    # do some regular expression to filter sql attacks
    # return clean expression (like no DROP or DELETE with no WHERE)
    # pass