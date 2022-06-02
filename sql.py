import MySQLdb

#connection 

conn = MySQLdb.connect(host='localhost',database='world',user='root',password='root')

cursor = conn.cursor()

cursor.execute("select * from emptab")

#getting all rows
row = cursor.fetchone()
while row is not None:
	print(row)
	row = cursor.fetchone()

cursor.close()
conn.close()