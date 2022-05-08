#Script to turn on a the pump when needed (Here print pressure status in a console box)

from tkinter import Tk, Button, Label, DoubleVar, Entry
import datetime

#GUI Window

window = Tk()
window.title('Automatic Air Pressure Checker')
window.configure(background='#EAF0CE')
window.geometry('445x200')
window.resizable(width=False,height=False)


# functions for the app

def power():
    pressure = float(pres_entry.get())
    
    if(pressure < 31):
        consolText.set('> Pressure increasing..')
        pres_value.set('31')  
    else:
        consolText.set('> Pressure is correct')
        pres_value.set('31')


        
def check():

    time = float(time_entry.get())
    if(time == 07.00):
        power()
    else:
        consolText.set('> Time should be 07.00!')



def clear():
    consolText.set('')
    time_value.set('')
    pres_value.set('')


# gui elements

#console
    #label
consol_lbl = Label(window, text='Console', bg='#EAF0CE', fg='#000000')
consol_lbl.grid(column=0, row=0)

    #console box      
consolText = DoubleVar()
consol = Entry(window, text=consolText, bg='#7D8491', fg='#FFFFFF', width=68)
consol.grid(column=0, row=1, padx=15)

#time
    #label
time_lbl = Label(window, text="Set Time", bg='#EAF0CE', fg="#000000", width=19)
time_lbl.grid(column=0, row=2)
    #entry widget
time_value=DoubleVar()
time_entry=Entry(window, textvariable=time_value, width=14)
time_entry.grid(column=0, row=3)
time_entry.delete(0, 'end')


#pressure
    #label
pres_lbl = Label(window, text='Set Pressure (PSI)', bg='#EAF0CE', fg='#000000',width=19)
pres_lbl.grid(column=0, row=4)
    #entry pressure
pres_value=DoubleVar()
pres_entry=Entry(window, textvariable=pres_value, width=14)
pres_entry.grid(column=0, row=5)
pres_entry.delete(0, 'end')




#Buttons
    #Check
check_btn = Button(window, text='Check', bg='#3F334D', fg='#FFFFFF', width=20, command=check)
check_btn.grid(column=0,row=6, pady=15)





window.mainloop()
