#Rewrite of the music player v1.0 with root window used
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from pygame import mixer
import musicFunctions as mF
import sv_ttk

mixer.init()

#variables

root = Tk()

#setting the theme
sv_ttk.set_theme('light')

#image files (light)
playL = PhotoImage(file = "resources/light/play.png")
stopL = PhotoImage(file = "resources/light/stop.png")
resumeL = PhotoImage(file = "resources/light/resume.png")
pauseL = PhotoImage(file = "resources/light/pause.png")
openL = PhotoImage(file = "resources/light/open.png")
closeL = PhotoImage(file = "resources/light/close.png")
infoL = PhotoImage(file = "resources/light/info.png")
githubL = PhotoImage(file = "resources/light/github.png")
musicL = PhotoImage(file = "resources/light/music.png")
loopL = PhotoImage(file = "resources/light/loop.png")
queueL = PhotoImage(file = "resources/light/queue.png")

#resize(ing) the images
pL = playL.subsample(2, 2)
sL = stopL.subsample(2, 2)
rL = resumeL.subsample(2, 2)
paL = pauseL.subsample(2, 2)
oL = openL.subsample(2, 2)
cL = closeL.subsample(2, 2)
iL = infoL.subsample(2, 2)
gL = githubL.subsample(2, 2)
lL = loopL.subsample(2, 2)
qL = queueL.subsample(2, 2)

###image files (dark)
##playD = PhotoImage(file = "resources/dark/play.png")
##stopD = PhotoImage(file = "resources/dark/stop.png")
##resumeD = PhotoImage(file = "resources/dark/resume.png")
##pauseD = PhotoImage(file = "resources/dark/pause.png")
##openD = PhotoImage(file = "resources/dark/open.png")
##closeD = PhotoImage(file = "resources/dark/close.png")
##infoD = PhotoImage(file = "resources/dark/info.png")
##githubD = PhotoImage(file = "resources/dark/github.png")
##musicD = PhotoImage(file = "resources/dark/music.png")
##loopD = PhotoImage(file = "resources/dark/loop.png")
##queueD = PhotoImage(file = "resources/dark/queue.png")
##
###resizing images
##pD = playD.subsample(2, 2)
##sD = stopD.subsample(2, 2)
##rD = resumeD.subsample(2, 2)
##paD = pauseD.subsample(2, 2)
##oD = openD.subsample(2, 2)
##cD = closeD.subsample(2, 2)
##iD = infoD.subsample(2, 2)
##gD = githubD.subsample(2, 2)
##lD = loopD.subsample(2, 2)
##qD = queueD.subsample(2, 2)

#variables for images
pImg = pL
sImg = sL
rImg = rL
paImg = paL
oImg = oL
cImg = cL
iImg = iL
gImg = gL
lImg = lL
qImg = qL

#menu
menubar = Menu(root)

songmenu = Menu(menubar, tearoff=0)
songmenu.add_command(label="Open", command=mF.browseFiles)
songmenu.add_separator()
songmenu.add_command(label="Exit", command=mF.exit)
menubar.add_cascade(label="File", menu=songmenu)

thememenu = Menu(menubar, tearoff=0)
thememenu.add_command(label="Light", command=mF.theme_set_light)
thememenu.add_command(label="Dark", command=mF.theme_set_dark)
menubar.add_cascade(label="Themes", menu = thememenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=mF.info)
helpmenu.add_command(label="Github", command=mF.github)
menubar.add_cascade(label="About", menu = helpmenu)

#UI
playButton = Button(root,
                        text="Play",
                        image = pImg,
                        compound = LEFT,
                        command=mF.play).grid(column=0,
                                                row=0,
                                                ipadx=11,
                                                ipady=5)

stopButton = Button(root,
                        text="Stop",   
                        image = sImg,
                        compound = LEFT,
                        command=mF.stop).grid(column=1,
                                               row=0,
                                               ipadx=5,
                                               ipady=5)

pauseButton = Button(root,
                         text="Pause",
                         image = paImg,
                         compound = LEFT,
                         command=mF.pause).grid(column=2,
                                                 row=0,
                                                 ipadx=5,
                                                 ipady=5)

resumeButton = Button(root,
                          text="Resume",
                          image = rImg,
                          compound = LEFT,
                          command=mF.resume).grid(column=3,
                                                   row=0,
                                                   ipadx=5,
                                                   ipady=5)

queueButton = Button(root,
                     text="Queue",
                     image = qImg,
                     compound = LEFT,
                     command=mF.queue).grid(column=0,
                                            row=1,
                                            ipadx=5,
                                            ipady=5)



root.config(menu=menubar)
root.mainloop()

