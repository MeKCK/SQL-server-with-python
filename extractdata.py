# using pandas read_sql
data = pd.read_sql("SELECT TOP(1000) * FROM customers", cnxn)

# returns a dataframe with top 1000 rows from customers table