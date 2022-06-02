#insert several rows from keyboard into emptab
import MySQLdb

def insert_rows(eno, ename, sal):
	conn = MySQLdb.connect(host = 'localhost', database = 'world', user = 'root', password = 'root')

	cursor = conn.cursor()

	str = "insert into emptab(eno, ename, sal) values('%d', '%s', '%f')"

	args = (eno, ename, sal)

	try:
		#execute sql query
		cursor.execute(str % args)

		#save changes to db
		conn.commit()
		print('1 row inserted...')

	except:
		#rollback if any error
		conn.rollback()

	finally:
		#close connection
		cursor.close()
		conn.close()

#enter rows from kb
n = int(input('Enter amount of rows: '))

for i in range(n):
	x = int(input("Enter eno: "))
	y = input('Enter name: ')
	z = float(input('Enter salary: '))
	#pass x y z in insert rows func
	insert_rows(x, y, z)
	print('----------------------------')