# to initialize a cursor
cursor = cnxn.cursor()

#selecting 1000 rows in table: customers
cursor.execute ("SELECT TOP(1000) * FROM customers")  #performs operation within server
#doesnt return data 