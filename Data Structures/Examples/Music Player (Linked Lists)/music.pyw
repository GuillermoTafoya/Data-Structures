import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from DataStructures import DoublyLinkedList
from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext 
from PIL import ImageTk,Image  

root = Tk()
root.title("Music Player")
root.geometry("600x400")
root.minsize(600, 400)
root.maxsize(600, 400)
root.iconbitmap(".\Resources\Tafoya.ico")

mixer.init()

mp3 = DoublyLinkedList()

class song:
    def __init__(self, Name, Image, Dir, Songs = None):
        self.name = Name
        self.image = Image
        self.dir = Dir
        self.songs = Songs

jazzSongs = DoublyLinkedList()

for i in (
    0.42, 230, 542.4, 706.5,
    926.2, 1200, 1510):
    jazzSongs.add(i)

#jazzSongs.printList()

currentNodeJazz = jazzSongs.head

mp3.add(default := song("None", img := ImageTk.PhotoImage(Image.open(
    ".\Resources\\titleBackground.jpg").resize((600, 390), Image.ANTIALIAS)),
    ""))

tracks= []
backgrounds= []
names = []
currentFile = os.getcwd() + "\Resources"

for folderName, subfolders, filenames in os.walk(currentFile):
    for subfolder in subfolders:
        names.append(subfolder)
    for filename in filenames:
        name, extension = os.path.splitext(filename)
        #print("Filenames. " + filename)
        if (extension == ".jpg" or extension == ".png") and filename != "titleBackground.jpg":
            backgrounds.append(filename)
        if extension == ".mp3" or extension == ".wav":
            tracks.append(filename)


#for i in names: 
#    print("Names: " + i)
#for i in tracks:
#    print("Tracks: " + i)
#for i in backgrounds:
#    print("BG: " + i)

for i in range(len(names)):
    mp3.add(song(names[i],  img := ImageTk.PhotoImage(Image.open(
        currentFile + "\\" + names[i] + "\\" + backgrounds[i]).resize((600, 390), Image.ANTIALIAS)),
        currentFile + "\\" + names[i] + "\\" + tracks[i]))

#Make it a circular list

mp3.head.next.prev = mp3.tail
mp3.tail.next = mp3.head.next

nowPlaying = mp3.head

#Handy functions

state = "Play"

def playPause(playing):
    global state
    if nowPlaying == mp3.head:
        start(playing)
        return
    if state == "Play":
        mixer.music.pause()
        state = "Pause"
    else: 
        mixer.music.unpause()
        state = "Play"

def start(playing):
    global nowPlaying
    nowPlaying = mp3.head.next
    mixer.music.load(nowPlaying.data.dir)
    mixer.music.play()
    songImage.itemconfig(img_id, image=nowPlaying.data.image)
    message = f"Now Playing: {nowPlaying.data.name}"
    playing.set(message)

def prevSong(songImage):
    global nowPlaying
    global currentNodeJazz
    global state
    state = "Play"
    if nowPlaying == mp3.search("Zelda Jazz", ".name").next:
        nowPlaying = nowPlaying.prev
        currentNodeJazz = jazzSongs.tail
        mixer.music.load(nowPlaying.data.dir)
        mixer.music.play()
        songImage.itemconfig(img_id, image=nowPlaying.data.image)
        mixer.music.set_pos(currentNodeJazz.data)
        message = f"Now Playing: {nowPlaying.data.name} {jazzSongs.index(currentNodeJazz.data) + 1}"
        playing.set(message)
        return
    elif nowPlaying == mp3.head:
        nowPlaying = mp3.tail
        currentNodeJazz = jazzSongs.tail
        mixer.music.load(nowPlaying.data.dir)
        mixer.music.play()
        songImage.itemconfig(img_id, image=nowPlaying.data.image)
        mixer.music.set_pos(currentNodeJazz.data)
        message = f"Now Playing: {nowPlaying.data.name} {jazzSongs.index(currentNodeJazz.data) + 1}"
        playing.set(message)
        return
    if nowPlaying.data.name == "Zelda Jazz" and currentNodeJazz.prev is not None:
        currentNodeJazz = currentNodeJazz.prev
        mixer.music.set_pos(currentNodeJazz.data)
        message = f"Now Playing: {nowPlaying.data.name} {jazzSongs.index(currentNodeJazz.data) + 1}"
        playing.set(message)
        return
    nowPlaying = nowPlaying.prev
    mixer.music.load(nowPlaying.data.dir)
    mixer.music.play()
    songImage.itemconfig(img_id, image=nowPlaying.data.image)
    setTitleScreenDefaultText(playing)

def nextSong(songImage):
    global nowPlaying
    global currentNodeJazz
    global state
    state = "Play"
    if nowPlaying == mp3.search("Zelda Jazz", ".name").prev:
        nowPlaying = nowPlaying.next
        mixer.music.load(nowPlaying.data.dir)
        mixer.music.play()
        songImage.itemconfig(img_id, image=nowPlaying.data.image)
        currentNodeJazz = jazzSongs.head
        message = f"Now Playing: {nowPlaying.data.name} {jazzSongs.index(currentNodeJazz.data) + 1}"
        playing.set(message)
        return
    if nowPlaying.data.name == "Zelda Jazz" and currentNodeJazz.next != jazzSongs.head:
        currentNodeJazz = currentNodeJazz.next
        mixer.music.set_pos(currentNodeJazz.data)
        message = f"Now Playing: {nowPlaying.data.name} {jazzSongs.index(currentNodeJazz.data) + 1}"
        playing.set(message)
        return
    nowPlaying = nowPlaying.next
    mixer.music.load(nowPlaying.data.dir)
    mixer.music.play()
    songImage.itemconfig(img_id, image=nowPlaying.data.image)
    setTitleScreenDefaultText(playing)

#Define frames


titleScreen = Frame(root, width=600, height=400)
searchBar = Frame(titleScreen)

titleScreen.place(relx = 0, rely = 0, relheight = 0.99, relwidth = 0.99)
searchBar.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 1)

songImage = Canvas(titleScreen, width=600, height=392)
songImage.place(relx=0, rely=0.2)

img_id = songImage.create_image((0, 0), image=nowPlaying.data.image, anchor="nw")

#titleScreen


def setTitleScreenDefaultText(playing):
    message = f"Now Playing: {nowPlaying.data.name}"
    playing.set(message)

playing = StringVar()

try:
    message = message = f"Now Playing: {nowPlaying.data.name}"
except:
    message = f"Now Playing: NA"

playing.set(message)

currentMP = Label(titleScreen, textvariable = playing, fg="white", bg="#0c0c0b")
currentMP.place(relx = 0 , rely = 0.1, relheight = 0.1, relwidth = 1)

#Play Bar                         



Button(searchBar, text="<<", command = lambda: prevSong(
    songImage)).grid(row = 0, column= 4)

Button(searchBar, text="Pause/Play", command=lambda: playPause(playing)).grid(row=0, column=5)

Button(searchBar, text=">>", command = lambda: nextSong(
    songImage)).grid(row = 0, column = 6)

if not mixer.get_busy:
    lambda: nextSong(songImage)

root.wm_attributes('-transparentcolor', 'grey')
titleScreen.tkraise()
searchBar.tkraise()
root.mainloop()
