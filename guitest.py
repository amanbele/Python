# Step 1)import necessary libraries/modules
from tkinter import Tk, Button, Label, DoubleVar, Entry


#create the application window and add configuration to window

window = Tk()
window.title('Feet To Meter Conversion App')
window.configure(background='light green')
window.geometry('320x220')
window.resizable(width=False,height=False)


# Step 3)create a functions for convert and clear

def convert():
    value=float(ft_entry.get())
    meter =value * 0.3048
    mt_value.set('%4f' %meter)

def clear():
    ft_value.set("")
    mt_value.set("")



# Step 2)adding lable, entery widgets, Buttons

#labels for feet
ft_lbl = Label(window, text='Feet', bg='purple', fg='white',width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

# entery widget for feet
ft_value=DoubleVar()
ft_entry=Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0,'end')




#label for meter
mt_lbl=Label(window, text='Meter', bg='brown',fg='white',width=14)
mt_lbl.grid(column=0, row=1)

#enetry widget for meter
mt_value=DoubleVar()
mt_entry=Entry(window, textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=30)
mt_entry.delete(0,'end')

#creating button for convert and clear
#convert
convert_btn = Button(window, text='Convert',bg='blue',fg='white',width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15) 

#clear
clear_btn=Button(window, text='Clear',bg='black',fg='white',width=14,command= clear)
clear_btn.grid(column=1, row=3, padx=15)




window.mainloop() 
