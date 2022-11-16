from tkinter import *
from pytube import YouTube

root=Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title('Youtube downloader')

Label(root, text="Free YouTube videos here", font='helvetica 14 bold').pack()
link=StringVar()
Label(root, text="Enter link below", font='helvetica 14').place(x=200,y=55)
Entry(root, width=50, textvariable=link).place(x=20,y=95)

Button(root, text='Download', font='helvetica 16 bold', bg='red', padx=2,command="download").place(x=100, y=150)

def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Downloaded', font='san-serif 14').place(x=100, y=120)

root.mainloop()
