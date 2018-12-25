#(b)	Write a python program to implement a class called Adder that exports a method 
#add(self, x, y) that prints a “Not Implemented” message. Then define two subclasses of Adder that implement the add method:
#1.	ListAdder, with an add method that returns the concatenation of its two list argu¬ments
#2.	DictAdder, with an add method that returns a new dictionary with the items in both its two dictionary arguments.
#3.	Overload the + operator

class Adder:
  def add(self,x,y):
    print("Not Implemented")
  def __init__(self,start=[]):
    self.data=start
  def __add__(self,other):
    self.data=self.data+other
    print(self.data)
  def __radd__(self,other):
    return self.add(self.data,other)

class listadder(Adder):
  def add(self,x,y):
    return x+y
class dictadder(Adder):
  def add(self,x,y):
    new={}
    for k in x.keys():
      new[k]=x[k]
    for k in y.keys():
      new[k]=y[k]
    return new
x=Adder()
print(x.add(1,2))
x=listadder()
print(x.add([1],[2]))
x=dictadder()
print(x.add({"a":"1"},{"b":"2"}))
x=Adder([1])
print(x+[3])
x=listadder([1])
print(x+[8])
print([2]+x)
