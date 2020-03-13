from db_products_oop import *

products_tb = NWProducts()

while True:

    print('select 1 for all products')
    print('select 2 for one product')
    print('select 3 for create a product')
    print('select 4 for remove a product')

    user_input = input('>>>')

    if user_input == '1':
        # get all our product using our new method
        # ITERATE ANd display them nicely
        data = products_tb.read_all()
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record.ProductID, record.ProductName)

    elif user_input == '2':
        chosen = input('enter product row: ')
        data = products_tb.read_one(chosen)
        record = data.fetchone()
        print(record)

    elif user_input == '3':
        product_name = input("Input ProductName: ")
        supplier_id = input("Input SupplierID: ")
        category_id = input("Input CategoryID: ")
        quantity = input("Input QuantityPerUnit: ")
        price = input("Input UnitPrice: ")
        stock = input("Input UnitsInStock: ")
        order = input("Input UnitsOnOrder: ")
        reorder = input("Input ReorderLevel: ")
        discontinued = input("Input Discontinued: ")
        products_tb.create_one(product_name, supplier_id, category_id, quantity, price, stock, order, reorder, discontinued)

    elif user_input == '4':
        remove = input("Input ProductID of product to remove: ")
        products_tb.delete_one(remove)
