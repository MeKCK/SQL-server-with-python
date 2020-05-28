cursor = cnxn.cursor()

#first altering the table, adding a column
cursor.execute("ALTER TABLE customer" +
               "ADD fullName VARCHAR(20)")

#now updating that column to contain firstName + lastName
cursor.execute(Update customer " +
               "SET fullName = firstName +" "+ lastName")

#commit changes to make them permanent 
cnxn.commit()