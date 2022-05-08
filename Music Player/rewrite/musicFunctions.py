#dk why i need to import stuff here as well :p
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from pygame import mixer
import sv_ttk

root = Tk()

""" #image files
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

#image files (dark)
playD = PhotoImage(file = "resources/dark/play.png")
stopD = PhotoImage(file = "resources/dark/stop.png")
resumeD = PhotoImage(file = "resources/dark/resume.png")
pauseD = PhotoImage(file = "resources/dark/pause.png")
openD = PhotoImage(file = "resources/dark/open.png")
closeD = PhotoImage(file = "resources/dark/close.png")
infoD = PhotoImage(file = "resources/dark/info.png")
githubD = PhotoImage(file = "resources/dark/github.png")
musicD = PhotoImage(file = "resources/dark/music.png")
loopD = PhotoImage(file = "resources/dark/loop.png")
queueD = PhotoImage(file = "resources/dark/queue.png")

#resizing images
pD = playD.subsample(2, 2)
sD = stopD.subsample(2, 2)
rD = resumeD.subsample(2, 2)
paD = pauseD.subsample(2, 2)
oD = openD.subsample(2, 2)
cD = closeD.subsample(2, 2)
iD = infoD.subsample(2, 2)
gD = githubD.subsample(2, 2)
lD = loopD.subsample(2, 2)
qD = queueD.subsample(2, 2)

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
 """

#functions file

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an audio file",
                                          filetypes = (("Audio Files", "*.mp3*"), ("All files", "*.*")))
    mixer.music.load(filename)

def info():
    messagebox.showinfo("Credit", credit)

def github():
    messagebox.showinfo("Github", github)

def exit():
    quit()

def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def queue():
    queuefile = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an audio file",
                                          filetypes = (("Audio Files", "*.mp3*"), ("All files", "*.*")))
    mixer.music.queue(queuefile)

def theme_set_light():
    sv_ttk.set_theme('light')
##    pImg = pL
##    sImg = sL
##    rImg = rL
##    paImg = paL
##    oImg = oL
##    cImg = cL
##    iImg = iL
##    gImg = gL
##    lImg = lL
##    qImg = qL

def theme_set_dark():
    sv_ttk.set_theme('dark')
##    pImg = pD
##    sImg = sD
##    rImg = rD
##    paImg = paD
##    oImg = oD
##    cImg = cD
##    iImg = iD
##    gImg = gD
##    lImg = lD
##    qImg = qD

#variables
credit = '''Program written by
Aman Bele.
Rewritten by me as well.'''
github = '''https://github.com/loungeclown
gotta change soon :D'''

