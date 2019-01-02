from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x500')
frame = Frame(root)
def red():
    messagebox.showinfo("Red Color","STOP")
def yellow():
    messagebox.showinfo("Yellow Color", "GET READY")
def green():
    messagebox.showinfo("Green Color", "GO")
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton = Button(frame, text='Red', fg='red', command=red)
redbutton.pack(side=LEFT)
yellowbutton = Button(frame, text='Yellow', fg='yellow', bg='black', command=yellow)
yellowbutton.pack(side=LEFT)
greenbutton = Button(frame, text='Green', fg='green', command=green)
greenbutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text='Black', fg='black', command=root.destroy)
blackbutton.pack(side=BOTTOM)
root.mainloop()
