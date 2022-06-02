import os
import time
from time import sleep
import tkinter as Tk
from tkinter import ttk
import sv_ttk
import datetime
from plyer import notification


root = Tk.Tk()

root.title('Task Scheduler')
root.geometry('468x256')
sv_ttk.set_theme('dark')

padding = {'padx': 5, 'pady': 5}
ipadding  = {'ipady': 10}

# variables
hour_var = Tk.StringVar()
min_var = Tk.StringVar()
sec_var = Tk.StringVar()
c_t_h_val = Tk.StringVar()
c_t_m_val = Tk.StringVar()
c_t_s_val = Tk.StringVar()

e = datetime.datetime.now()

# current time
ttk.Label(root, text = 'Current Time').grid(column = 0, row = 0)
cur_time_hour = ttk.Button(root, textvariable = c_t_h_val).grid(column = 0, row = 1)
cur_time_min = ttk.Button(root, textvariable = c_t_m_val).grid(column = 1, row = 1)
cur_time_hour = ttk.Button(root, textvariable = c_t_s_val).grid(column = 2, row = 1)

# input
ttk.Label(root, text = 'Set Time').grid(column = 0, row = 2)
hour_ent = ttk.Entry(root, textvariable = hour_var).grid(column = 0, row = 3)
min_ent = ttk.Entry(root, textvariable = min_var).grid(column = 1, row = 3)
sec_ent = ttk.Entry(root, textvariable = sec_var).grid(column = 2, row = 3)

def notify_timeup():
	notification.notify(
	    title='Here is the title',
	    message='Here is the message',
	    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
	    timeout=10,  # seconds
		)

def countdowntimer():

   times = int(hour_var.get())*3600+ int(min_var.get())*60 + int(sec_var.get())

   while times > -1:

      minute,second = (times // 60 , times % 60)
      hour = 0

      if minute > 60:
         hour , minute = (minute // 60 , minute % 60)
      sec_var.set(second)
      min_var.set(minute)
      hour_var.set(hour)

      # Update the time
      root.update()
      sleep(1)
      if(times == 0):
         sec_var.set('00')
         min_var.set('00')
         hour_var.set('00')
      times -= 1

temp = ttk.Button(root, text='start', command = countdowntimer).grid(column = 0, row = 4)

root.mainloop()