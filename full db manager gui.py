#Program to manage database
'''Features:
Adding rows
Deleting rows
Updating rows
viewing rows
changing dbs and lot more'''
import mysql.connector
import MySQLdb

# function to display db
def display_db():
	# user input values
	print('Dafault [localhost]')
	hostname = input('Enter your hostname: ')
	username = input('Enter your username: ')
	passname = input('Enter your password: ')

	if hostname == '':
		hostname = 'localhost'
	else:
		pass

	# connect to db
	conn = mysql.connector.connect (user=username, password=passname,
	                               host=hostname,buffered=True)	
	cursor = conn.cursor()
	databases = ("show databases")
	cursor.execute(databases)
	for (databases) in cursor:
	     print(databases[0])

display_db()



	



