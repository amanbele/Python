from plyer import notification 
import tkinter as tk
from tkinter import ttk, filedialog
import sv_ttk

root = tk.Tk()
root.geometry('230x220')
root.title('Notification Generator')
sv_ttk.set_theme('dark')

title_var = tk.StringVar()
msg_var = tk.StringVar()
filename = None
dura_var = tk.IntVar()

def notify_timeup():
  notification.notify(
      title = title_var.get(),
      message = msg_var.get(),
      app_icon = filename,  # e.g. 'C:\\icon_32x32.ico'
      timeout = dura_var.get() # seconds
    )

def update_fn():
  file_name = filename

def browseFiles():
  file_name = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
  update_fn()

padding = {'padx': 5, 'pady': 5}


ttk.Label(root, text = 'Title').grid(column = 0, row = 0, **padding)
title = ttk.Entry(root, textvariable = title_var).grid(column = 1, row = 0, **padding)

ttk.Label(root, text = 'Message').grid(column = 0, row = 1, **padding)
msg = ttk.Entry(root, textvariable = msg_var).grid(column = 1, row = 1, **padding)

ttk.Label(root, text = 'Icon File').grid(column = 0, row = 2, **padding)
icon = ttk.Button(root, text = 'Browse', command = browseFiles).grid(column = 1, row = 2, **padding)

ttk.Label(root, text = 'Duration').grid(column = 0, row = 3, **padding)
dura = ttk.Entry(root, textvariable = dura_var).grid(column = 1, row = 3, **padding)

ttk.Button(root, text = 'Generate', command = notify_timeup).grid(column = 1, row = 4, **padding)

root.mainloop()