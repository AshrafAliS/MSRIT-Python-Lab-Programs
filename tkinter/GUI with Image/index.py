from tkinter import *
from main import *
from std import *

root = Tk()
root.geometry('500x400')
root.title("Ramaiah Institute of Technology")

logo = PhotoImage(file="images/logo500x500.png")
frame1 = Frame(root)
frame1.pack()
Label(frame1, image=logo, bg="black").pack(side=TOP)
canvas = Canvas(frame1)
canvas["width"] = 200
canvas["height"] = 100
canvas.pack(side=LEFT)

label = Label(root, text="SELECT PROFILE", width=20, font=("bold", 20))
label.place(x=90, y=100)

Button(root, text='Faculty', width=20, bg='brown', fg='white', command=faculty).place(x=180, y=180)
Button(root, text='Student', width=20, bg='brown', fg='white', command=student).place(x=180, y=250)

root.mainloop()
