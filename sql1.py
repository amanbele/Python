import MySQLdb

#connect
conn = MySQLdb.connect(host = 'localhost', database = 'world', user = 'root', password = 'root')

cursor = conn.cursor()

# cursor.execute('select * from emptab')

# rows = cursor.fetchall()

# print('Total number of rows = ', cursor.rowcount)

# for row in rows:
# 	eno = row[0]
# 	ename = row[1]
# 	sal = row[2]
# 	print('%-6d %-15s %10.2f'% (eno, ename, sal))





def insert_rows(eno, ename, sal):
	args = (eno, ename, sal)

	str = "insert into emptab(eno, ename, sal) values('%d', '%s', '%f')"

	try:
		#execute method
		cursor.execute(str % args)

		#save changes to database
		conn.commit()
		print('1 row inserted...')

	except:
		#rollback if there is any error
		conn.rollback()

insert_rows(1202, 'aman', 100000000)

#close connection
cursor.close()
conn.close()

