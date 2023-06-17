from pytube import YouTube
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import PyPDF2
from PIL import Image, ImageTk
from tkinter import Entry
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=50)
canvas.grid(columnspan=3)
root.resizable(False, False)

button_image = PhotoImage(
    file="C:\\Users\\abelh\OneDrive\Desktop\\video gio downloadeder\\buttom.png"
)


root.title("Youtube Downloader")
root.iconbitmap("C:\\Users\\abelh\OneDrive\Desktop\\video gio downloadeder\\c.ico")
l1 = Label(
    text="Enter Your Url : ",
    font=55,
)
l1.grid(row=0, column=0)


e1 = Entry(root, width=120, bd=10, fg="blue")
e1.grid(row=0, column=0)


def c1():
    b1.configure(text="Found it", fg="white")
    url = e1.get()
    x = Label(
        text="Any error your (URL) wrong!",
        font=40,
        bg="red",
    )
    x.grid(
        row=0,
        column=0,
    )
    x.place(
        x=10,
        y=50,
    )
    yt = YouTube(url)
    vids = yt.streams.all()
    for i in range(len(vids)):
        e2 = Label(height=2)
        e2.grid(row=i + 2, column=0)
        e2.configure(text=f"{i}. {vids[i]}")

    e3 = Entry(root, fg="red")
    e3.grid(row=i + 4)
    b1.configure(text="Submit", fg="green")

    def c2():
        location = filedialog.askdirectory()

        print(location)
        vnum = int(e3.get())
        vids[vnum].download(rf"{location}")
        b3.configure(text="Done✔")
        # time.sleep(140)
        # b3.configure(text="Save")

    c123 = Label(text="Choose number : ", fg="green", font=40)
    c123.grid(
        row=i + 3,
        column=0,
    )
    b3 = Button(
        root,
        text="Save",
        font=("Arial Black",),
        fg="red",
        command=c2,
        image=button_image,
        compound="center",
        bd=0,
    )
    b3.grid(row=i + 6, column=0)


b1 = Button(
    root,
    text="Submit",
    font=("Arial Black",),
    fg="green",
    command=c1,
    bd=0,
    image=button_image,
    compound="center",
)


def buttom_hover():
    b1["fg"] = "red"


b1.bind(
    "<Enter>",
)

b1.grid(row=1, column=0)


# vnum = int(input("Enter vid num: "))
# vids[vnum].download(r"C:\Download Mp3")
# print("done")


root.mainloop()
