<h1>MSRIT Python Programmng Lab</h1>
<h3>Procedure</h3>
<ul>
  <li>We Will Import <b>tkinter</b> for the GUI     (<i><b>from tkinter import *</b></i>)</li>
  <li>Also We Will Import sqlite 3 for Database Purpose   (<i><b>import sqlite3</b></i>)</li>
  <li>Then We Have To Create a Database for The Project    (<i><b>database = Database("student.db")</b></i>)</li>
</ul>
<hr>
<ul>
<li><p>In Our Program in the <b>Main.py</b> we are importing tkinter</p></li>
<li><p>in Second Line we are executing <b><i>from backend import Database</i></b> here <b>backend</b> is the filename called <b>backend.py</b> and Database is the <i>Class</i> name in backend.py file</p></li>
<li>We are creating a database as <b><i>database = Database("student.db")</i></b> which in turn create a <i>student.db</i> file in the current folder</li>
<hr>
<li>In the <i>Window(object)</i> We are creating a <i>window = Tk()  &nbsp;&nbsp;Window(window)</i> we can replace <i>window = Tk()</i> as <b>root=Tk()</b></li>
<li>for the Window we a assigning the title by using <b>self.window.wm_title("Student Management System")</b></li>
<li>we a setting the Window size by <b>self.window.geometry('500x500')</b></li>
<li>We Will Design a GUI using tkinter</li>
<hr>
  <li>If the user Entry as <b>self.e1 = Entry(window, textvariable=self.usn)</b> we will assign the entry as <i>StringVar</i> function as <b>self.usn = StringVar()</b> so that we are accepting the Sring value from the Entry(INPUT) field </li>
  <li>for Button <i>b1 = Button(window, text="View all", width=12, command=self.view_command)</i> the command as <b>self.view_command</b> will call a function <i>self.view_command()</i> function</li>
  <hr>
  <li>we have a function called <b>get_selected_row(self,event)</b> which will select the row which we want to access, and we will hide the first index of an array which is ID in the Database</li>
  <li>
    <ul>
      <h2>Insert Operation</h2>
      <li>we hav e a function called <b>add_command(self)</b> which will do the insert operation</li>
      <li>in the above function we have <b>database.insert(self.usn.get(), self.name.get(), self.mobile.get(), self.branch.get())</b></li>
      <li>which will pass the usn, name, mobile,, branch to the <i>database</i><li>
    </ul>
  </li>
</ul>
