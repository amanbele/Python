from tkinter import *
import qrcode
import sv_ttk


root = Tk()
root.title('PyQR Generator')
root.geometry('250x250')
sv_ttk.set_theme("light")

data_var = StringVar()


data_lbl = Label(root, text = 'Data ').grid(row = 0, column = 0)
data_entry = Entry(root, textvariable = data_var).grid(row=0, column=1)
data_gen = Button(root, text = 'Generate', command = None).grid(row = 0, column = 2, ipadx = 17)






root.mainloop()