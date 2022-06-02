import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='localhost', database='world')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("SELECT DATABASE()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()