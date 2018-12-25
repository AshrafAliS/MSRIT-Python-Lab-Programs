#(b)	Write a python program to calculate the area of the circle and catch appropriate user defined exception.(Hint: check for invalid radius)
import math
try:
    n=int(input("Enter Radius: "))
    if n<0:
       raise RuntimeError()
except:
        print('Invalid radius', RuntimeError('No characters Please','Non Negative Number'))
else:    
    try:
        print(math.pi*n*n)
    except RuntimeError as ex:
        print("Invalid radius,", ex)
