import pyodbc

# setup variables
server = '127.0.0.1:1433'
database = 'Northwind'
username = 'SA'
passwords = 'Passw0rd2018'

# make connection
conn = pyodbc.connect('DSN=MYMSSQL;UID=' + username + ';PWD=' + passwords + ';' + 'DATABASE=' + database)

# Creating a cursor object from connection
# Imagine like a real cursor on your azure data studio
# This will maintain state
crsr = conn.cursor()

# Running SQL Queries using .execute()
rows = crsr.execute("select * FROM CUSTOMERS")

# Cursor maintains state
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
# row = crsr.fetchone() # gets the next entry in the cursor
# print(row)
#
# # each row, has all the columns of that entry.
# # getting individual data is easy from this row
# print(row.CompanyName)
# print(row.ContactName)
# print(row.Fax)
#
# # Checking the headers of the columns
# print(crsr.description)
#
# print(type(crsr))
# print(type(row))


# using the fetchall() is dangerous
# using fetchall() is dangerous because you can stall/crash your servers
# if there is a lot of data :) and it will bottle neck the system
crsr.execute("select * FROM Customers")
all_rows = crsr.fetchall()
print(all_rows)
print(type(all_rows))


counter = 0
for item in all_rows:
    # print(item)
    counter += 1
    print(counter, item.ContactName, '-', 'Fax:', item.Fax)

# Best practices is to use a while loop and fetchone()
# Until your entry is none.
rows = crsr.execute("select * FROM Customers")
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.ContactName)


# Another example of while loop with fetch one but on products table
rows = crsr.execute("SELECT * FROM Products")
new_values =[]
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice * 200)
    new_values.append(record.UnitPrice * 200)

print(new_values)
