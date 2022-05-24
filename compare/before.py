# A timer program modified by Aman Bele as per Arpit Thakur's request (;
# proof? well see the upload time on @amanbele 's repo and ^ person's repo (;
# you cant do anything about this arpit btw haha
# also you can compare both releases

from tkinter import *
from tkinter import filedialog
import time
from pygame import mixer

mixer.init()

root = Tk()
root.geometry('400x300')
root.resizable(0,0)
root.config(bg ='blanched almond')
root.title('Countdown Clock And Timer')
Label(root, text = 'Made by Arpit Rajput' , font = 'arial 20 bold',  bg ='orange').pack()

Label(root,
    font ='arial 15 bold',
    text = 'current time :',
    bg = 'yellow').place(x = 40 ,y = 70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)

def browsefiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an Audio File",
                                          filetypes = (("Audio files", "*.mp3*"), ("All files", "*.*" )))
    mixer.music.load(filename)

curr_time =Label(root,
    font ='arial 15 bold',
    text = '',
    fg = 'black',
    bg ='papaya whip').place(x = 190 , y = 70)
clock()

sec = StringVar()
Entry(root,
    textvariable = sec,
    width = 2,
    font = 'arial 12').place(x=250, y=155)
sec.set('00')

mins= StringVar()
Entry(root,
    textvariable = mins,
    width =2,
    font = 'arial 12').place(x=225, y=155)
mins.set('00')

hrs= StringVar()
Entry(root,
    textvariable = hrs,
    width =2,
    font = 'arial 12').place(x=200, y=155)
hrs.set('00')

def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
      
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
   
        root.update()
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
            mixer.music.play()
        times -= 1

Label(root,
    font ='arial 15 bold',
    text = 'set the time',
    bg ='papaya whip').place(x = 40 ,y = 150)
Button(root,
    text='START',
    bd ='5',
    command = countdown,
    bg = 'antique white',
    font = 'arial 10 bold').place(x=150, y=210)
Button(root,
    text = 'Add an Audio File',
    bd = '5',
    command = browsefiles,
    bg = 'antique white',
    font = 'arial 10 bold').place(x=150, y = 240)

    
root.mainloop()
