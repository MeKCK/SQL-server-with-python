# accessing db over a trusted network 
 
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=UKXXX00123, 45600;"
            "Database=DB01;"
            "Trusted_Connection=yes;")

# accessing over non-secure network login (pass and username included)
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=UKXXX00123,45600;"
            "Database=DB01;"
            "UID=JoeBidden;"
            "PWD=Password123;")

#initialize connection 
cnxn = pyodbc.connect(cnxn_str)

