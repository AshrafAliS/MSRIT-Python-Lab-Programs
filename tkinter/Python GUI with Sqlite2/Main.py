from tkinter import *
from back import Database

database = Database("student.db")

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Student Management System")
        self.window.geometry('500x500')

        l1 = Label(window, text="USN")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="NAME")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="MOBILE")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="BRANCH")
        l4.grid(row=1, column=2)

        self.usn = StringVar()
        self.e1 = Entry(window, textvariable=self.usn)
        self.e1.grid(row=0, column=1)

        self.name = StringVar()
        self.e2 = Entry(window, textvariable=self.name)
        self.e2.grid(row=0, column=3)

        self.mobile = StringVar()
        self.e3 = Entry(window, textvariable=self.mobile)
        self.e3.grid(row=1, column=1)

        self.branch = StringVar()
        self.e4 = Entry(window, textvariable=self.branch)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=16, width=40)
        self.list1.grid(row=3, column=0, rowspan=6, columnspan=2)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=3, column=3)

        b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=4, column=3)

        b3 = Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=5, column=3)

        b4 = Button(window, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=6, column=3)

        b5 = Button(window, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=7, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=8, column=3)


    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.usn.get(), self.name.get(), self.mobile.get(), self.branch.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.usn.get(), self.name.get(), self.mobile.get(), self.branch.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.usn.get(), self.name.get(), self.mobile.get(), self.branch.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0],self.usn.get(), self.name.get(), self.mobile.get(), self.branch.get())
        self.view_command()

window = Tk()
Window(window)

window.mainloop()
