from tkinter import *
from pytube import YouTube

import logging
from threading import Thread
from json import JSONDecoder

#Create program frame
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube video downloader")
Label(root,text = 'Youtube Videolio Downloader', font ='arial 20 bold').pack()

#enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

#Text entry boxes
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

#functions to download videos of various qualities
def BestDownloader():
     
    url =YouTube(str(link.get()))
    #video = url.streams.first()
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 300)

def Downloader1080():
     
    url =YouTube(str(link.get()))
    #video = url.streams.first()
    video = url.streams.filter(res="1080p").first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 300)

def Downloader720():
     
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="720p").first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 300)

def Downloader480():
     
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="480p").first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 300)

def Downloader360():
     
    url =YouTube(str(link.get()))
    video = url.streams.filter(res="360p").first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 300) 


Button(root,text = 'Best Quality', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = BestDownloader).place(relx=0.25,rely=0.65, anchor=S)
Button(root,text = '1080p', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 3, command = Downloader1080).place(relx=0.5,rely=0.65, anchor=S)
Button(root,text = '720p', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 4, command = Downloader720).place(relx=0.68,rely=0.65, anchor=S)
Button(root,text = '480p', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 5, command = Downloader480).place(relx=0.4,rely=0.8, anchor=S)
Button(root,text = '360p', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 6, command = Downloader360).place(relx=0.6,rely=0.8, anchor=S)

root.mainloop()
