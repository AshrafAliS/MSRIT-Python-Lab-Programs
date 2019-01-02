from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x500')
root.title("Traffic Signal")

MyButton1 = Button(root, text="BUTTON1", width=10)
MyButton1.grid(row=0, column=0)

MyButton2 = Button(root, text="BUTTON2", width=10)
MyButton2.grid(row=0, column=1)

MyButton3 = Button(root, text="BUTTON3", width=10)
MyButton3.grid(row=0, column=2)

MyButton4 = Button(root, text="BUTTON4", width=10)
MyButton4.grid(row=1, column=2)

root.mainloop()
