#Music Player
#import all stuff needed
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from pygame import mixer


#Initialise mixer
mixer.init()


#variables
creditApp = '''Program written by
Aman Bele.
Using PyGame and Tkinter.'''
githubApp = '''My Github :D
https://github.com/loungeclown
'''


#functions
def infoshow():
    messagebox.showinfo("Credit", creditApp)
def playsong():
    mixer.music.play()
def stopsong():
    mixer.music.stop()
def pausesong():
    mixer.music.pause()
def resumesong():
    mixer.music.unpause()
def exitprogram():
    quit()
def github():
    messagebox.showinfo("Github", githubApp)
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Audio Files", "*.mp3*"), ("All files", "*.*")))
    mixer.music.load(filename)


#Window Configuration

window=ThemedTk(theme="equilux")
window.geometry("488x213+700+200")
window.configure(bg="#6b6b6b")
window.title("Music Player")
window.resizable(width=False,height=False)


#image files
playImg = PhotoImage(file = "resources/play.png")
stopImg = PhotoImage(file = "resources/stop.png")
resumeImg = PhotoImage(file = "resources/resume.png")
pauseImg = PhotoImage(file = "resources/pause.png")
openImg = PhotoImage(file = "resources/open.png")
closeImg = PhotoImage(file = "resources/close.png")
infoImg = PhotoImage(file = "resources/info.png")
githubImg = PhotoImage(file = "resources/github.png")
musicImg = PhotoImage(file = "resources/music.png")


#resize(ing) the images
pImg = playImg.subsample(2, 2)
sImg = stopImg.subsample(2, 2)
rImg = resumeImg.subsample(2, 2)
paImg = pauseImg.subsample(2, 2)
oImg = openImg.subsample(2, 2)
cImg = closeImg.subsample(2, 2)
iImg = infoImg.subsample(2, 2)
gImg = githubImg.subsample(2, 2)


#setting window icon
window.iconphoto(False, musicImg)


#buttons
openButton = ttk.Button(window,
                        text="Open",
                        image = oImg,
                        compound = LEFT,
                        command=browseFiles).grid(column=0,
                                                  row=0,
                                                  ipadx=5,
                                                  ipady=5)

creditButton = ttk.Button(window,
                          text="Credit",
                          image = iImg,
                          compound = LEFT,
                          command=infoshow).grid(column=1,
                                                 row=0,
                                                 ipadx=5,
                                                 ipady=5)

exitButton = ttk.Button(window,
                        text="Exit",
                        image = cImg,
                        compound = LEFT,
                        command=exitprogram).grid(column=2,
                                                  row=0,
                                                  ipadx=5,
                                                  ipady=5)

githubButton = ttk.Button(window,
                        text="Github",
                        image = gImg,
                        compound = LEFT,
                        command=github).grid(column=3,
                                                  row=0,
                                                  ipadx=5,
                                                  ipady=5)


#seperator labels
empty_label = ttk.Label(window, text="                            ").grid(column=0, row=1, ipadx=18, ipady=50)
empty_label1 = ttk.Label(window, text="                            ").grid(column=1, row=1, ipadx=18, ipady=50)
empty_label2= ttk.Label(window, text="                            ").grid(column=2, row=1, ipadx=18, ipady=50)
empty_label3 = ttk.Label(window, text="                            ").grid(column=3, row=1, ipadx=18, ipady=50)


#controls
playButton = ttk.Button(window,
                        text="Play",
                        image = pImg,
                        compound = LEFT,
                        command=playsong).grid(column=0,
                                               row=7,
                                               ipadx=5,
                                               ipady=5)

stopButton = ttk.Button(window,
                        text="Stop",
                        image = sImg,
                        compound = LEFT,
                        command=stopsong).grid(column=1,
                                               row=7,
                                               ipadx=5,
                                               ipady=5)

pauseButton = ttk.Button(window,
                         text="Pause",
                         image = paImg,
                         compound = LEFT,
                         command=pausesong).grid(column=2,
                                                 row=7,
                                                 ipadx=5,
                                                 ipady=5)

resumeButton = ttk.Button(window,
                          text="Resume",
                          image = rImg,
                          compound = LEFT,
                          command=resumesong).grid(column=3,
                                                   row=7,
                                                   ipadx=5,
                                                   ipady=5)




window.mainloop()
