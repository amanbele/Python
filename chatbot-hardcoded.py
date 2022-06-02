import tkinter as tk
from tkinter import ttk
import sv_ttk

root = tk.Tk()
root.geometry('200x400')
sv_ttk.set_theme('dark')

# variables
ipad = {'ipadx':5, 'ipady':5}
pad = {'padx':5, 'pady':5}
output_var = tk.StringVar()



# output
output_frame = tk.Frame(root).grid(row = 0, column = 0)
ttk.Entry(output_frame, textvariable = output_var).grid(row = 0, column = 0, ipadx = 17, ipady = 30, **pad)

# buttons
button_frame = tk.Frame(root).grid(row = 1, column = 1)
ttk.Button(button_frame, text = '+').grid(row = 1, column = 0, **ipad, **pad)
ttk.Button(button_frame, text = '-').grid(row = 1, column = 1, **ipad, **pad)

output_var.set('fed')

root.mainloop()

