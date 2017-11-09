import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : "+str(data))

# disconnect from server
db.close()