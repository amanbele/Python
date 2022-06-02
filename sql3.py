# Program to delete a row from emptab table by 
# accepting eno

import MySQLdb

# function to delete row from emptab
def delete_rows(eno):

	# connect to MySQL database
	conn = MySQLdb.connect(host = 'localhost',
		database = 'world',
		user = 'root',
		password = 'root')

	# prepare a cursor obj using cursor() method
	cursor = conn.cursor()

	# prepare sql query string to delete a row
	str = "delete from emptab where eno = '%d'"

	# define the args
	args = (eno)

	try:
		# execute the sql query using execute() method
		cursor.execute(str % args)

		#save the changes to the database
		conn.commit()
		print('1 row deleted...')

	except:
		# rollback if there is any error
		conn.rollback()

	finally:
		#close connection
		cursor.close()
		conn.close()

# enter eno whose row is to be deleted
x = int(input('Enter eno: '))

# pass eno to delete_rows() func
delete_rows(x)