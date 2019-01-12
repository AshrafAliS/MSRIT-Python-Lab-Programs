from tkinter import *
import sqlite3


def student():
    root1 = Tk()
    root1.geometry('500x400')
    root1.title("Ramaiah Institute of Technology")

    label = Label(root1, text="Student Login", width=20, font=("bold", 20))
    label.place(x=90, y=53)

    FullName = Label(root1, text="FullName", width=20, font=("bold", 10))
    FullName.place(x=80, y=130)

    Name = StringVar()
    entryFullName = Entry(root1, textvariable=Name)
    entryFullName.place(x=240, y=130)

    labelPassword = Label(root1, text="Email", width=20, font=("bold", 10))
    labelPassword.place(x=68, y=180)

    Password = StringVar()
    entryPassword = Entry(root1, textvariable=Password)
    entryPassword.place(x=240, y=180)

    Button(root1, text='Login', width=20, bg='brown', fg='white', command=Login).place(x=180, y=220)

    root1.mainloop()


def Login():
    print("Student Login in Functions")
