#Write a python program to create package ‘Sample ‘with 2 modules called stack and main,
#the stack module should have the following functions
#1) Getstack()- to return an empty stack
#2) Isempty()- to return true if stack is empty
#3) Top() – to return the index of stack top
#4) Push()- To push elements into a stack
#5) Pop()- to return top of stack element if stack is not empty
#6) The main module should use functions of the stack module to push and pop elements.

from 7a import stack
print("Empty Stack")
print(stack.GetStack())
print("1.Push\n2.Pop\n3.Is Empty\n4.Top")
while 1:
    n=int(input("Enter Your Choice"))
    if(n==1):
        item=input("Enter Element: ")
        stack.push(item)
    if(n==2):
        print(stack.pop())
    if(n==3):
        print(stack.isEmpty())
    if(n==4):
        print(stack.top())
    if(n==-1):
break
