# Python database manager
import mysql.connector
import tkinter as Tk
from tkinter import ttk, messagebox
import sv_ttk
from time import sleep

class App(Tk.Tk):

	# __init__ func
	def __init__(self):

		super().__init__()

		# window properties
		self.title('PyShopManager - Idle')
		self.geometry('512x512')
		sv_ttk.set_theme('dark')

		self.host_name = Tk.StringVar()
		self.db_name = Tk.StringVar()
		self.usr_name = Tk.StringVar()
		self.pas_word = Tk.StringVar()
		self.conn_btn_lbl = Tk.StringVar()
		self.result_val = Tk.StringVar()
		self.search_var = Tk.StringVar()

		self.item_id_var = Tk.IntVar()
		self.item_name_var = Tk.StringVar()
		self.item_prc_var = Tk.IntVar()
		self.item_cat_var = Tk.StringVar()

		self.create_ui()

	def create_ui(self):

		padding = {'padx': 5, 'pady': 5}
        # hostname
		host_lbl = ttk.Label(self, text = 'Hostname ').grid(column = 0, row = 0, **padding)
		host_ent = ttk.Entry(self, textvariable = self.host_name).grid(column = 1, row = 0, **padding)

		# database 
		db_lbl = ttk.Label(self, text = 'Database ').grid(column = 0, row = 1, **padding)
		db_ent = ttk.Entry(self, textvariable = self.db_name).grid(column = 1, row = 1, **padding)

		# user_name
		usr_lbl = ttk.Label(self, text = 'Username ').grid(column = 0, row = 2, **padding)
		usr_ent = ttk.Entry(self, textvariable = self.usr_name).grid(column = 1, row = 2, **padding)

		# password
		pas_lbl = ttk.Label(self, text = 'Password ').grid(column = 0, row = 3, **padding)
		pas_ent = ttk.Entry(self, textvariable = self.pas_word).grid(column = 1, row = 3, **padding)

		# connect button
		self.conn_btn_lbl.set('Connect')
		conn_btn = ttk.Button(self, textvariable = self.conn_btn_lbl, command = self.connect).grid(column = 0, row = 4, **padding)

		
		
		# <--------output lbl------------>
		output_lbl = ttk.Label(self, text = 'Output:                     ').grid(column = 2, row = 0, **padding)
		result_lbl = ttk.Label(self, textvariable = self.result_val).grid(column = 2, row = 1, **padding)

		# <--------menu-------->
		menubar = Tk.Menu(self)

		# <<---dbmenu--->>
		db_menu = Tk.Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = 'Database', menu = db_menu)
		db_menu.add_command(label = 'Show Tables', command = self.show_tables)

		# <------search stuff------>
		search_lbl = ttk.Label(self, text = 'Search').grid(column = 0, row = 5, **padding)
		search_ent = ttk.Entry(self, textvariable = self.search_var).grid(column = 1, row = 5, **padding)
		search_btn = ttk.Button(self, text = 'Search', command = self.search_item).grid(column = 2, row = 5, **padding)

		# <------item--------->
		ttk.Label(self).grid(column = 0, row = 6)

		item_id_lbl = ttk.Label(self, text = 'ID').grid(column = 0, row = 7, **padding)
		item_id_ent = ttk.Entry(self, textvariable = self.item_id_var).grid(column = 1, row = 7, **padding)

		item_name_lbl = ttk.Label(self, text = 'Name').grid(column = 0, row = 8, **padding)
		item_name_ent = ttk.Entry(self, textvariable = self.item_name_var).grid(column = 1, row = 8, **padding)

		item_prc_lbl = ttk.Label(self, text = 'Price').grid(column = 0, row = 9, **padding)
		item_prc_ent = ttk.Entry(self, textvariable = self.item_prc_var).grid(column = 1, row = 9, **padding)

		item_cat_lbl = ttk.Label(self, text = 'Category').grid(column = 0, row = 10, **padding)
		item_cat_ent = ttk.Entry(self, textvariable = self.item_cat_var).grid(column = 1, row = 10, **padding)

		# <----item operations--------->

		add_item_btn = ttk.Button(self, text = 'Add', command = self.add_item).grid(column = 2, row = 7, **padding)


		self.config(menu = menubar)

	def connect(self):

		padding = {'padx': 5, 'pady': 5}
		host_id = self.host_name.get()
		db_id = self.db_name.get()
		usr_id = self.usr_name.get()
		pas_id = self.pas_word.get()

		if host_id == '':
			self.host_name.set('localhost')

		conn_success = "Connection Information:\n Host: " + host_id + "\n Username: " + usr_id + "\n Password: " + pas_id + "\n Database: " + db_id 

		def conn_suc():
			self.title('PyShopManager - Connected')
			self.conn_btn_lbl.set('Connected')
			messagebox.showinfo('Connection Successful!', conn_success)

		def conn_ab():
			self.title('PyShopManager - Connection Aborted')
			self.conn_btn_lbl.set('Connection\nAborted')
			messagebox.showerror('Connection Aborted', 'One or all of your inputs are wrong!')
			sleep(3)
			self.title('PyShopManager - Idle')
			self.conn_btn_lbl.set('Connect')

		try:
			# establishing the connection
			self.conn = mysql.connector.connect(user=usr_id, password=pas_id, host=host_id, database=db_id)

			# Creating a cursor object using the cursor() method
			self.cursor = self.conn.cursor()

			# Executing an MYSQL function using the execute() method
			self.cursor.execute("SELECT DATABASE()")

			# Fetch a single row using fetchone() method.
			data = self.cursor.fetchone()
			# connection successfull indicator
			conn_suc()

		except:
			# connection un-successfull indicator
			conn_ab()

	# show all tables in a db
	def show_tables(self):

		try:
			self.cursor = self.conn.cursor()

			self.cursor.execute("SHOW TABLES")

			for table_name in self.cursor:
			   table_var = (table_name)

			self.result_val.set(table_var)
		except AttributeError:
			self.result_val.set('Please try connecting\nwith database first!')

	def search_item(self):
		
		try:
			name = self.search_var.get()
			search_res = self.cursor.execute("SELECT * from products WHERE name = %s", (name,))
			self.result_val.set(search_res)
		except:
			self.result_val.set('Error!')

	def add_item(self):
		add_str = ("""INSERT INTO products (id, name, price, category) VALUES (%s, %s, %s, %s)""")

		# input
		i = self.item_id_var.get()
		n = self.item_name_var.get()
		p = self.item_prc_var.get()
		c = self.item_cat_var.get()

		if i == '':
			i = i+1
		if n == '':
			n = 'none'
		if p == '':
			p = 1
		if c == '':
			p = 'General'

		data_item = (i, n, p, c)

		# insert new item

		self.cursor.execute(add_str)
		self.result_val.set('1 row inserted...')

		# commiting data
		self.conn.commit()



if __name__ == "__main__":
	app = App()
	app.mainloop()