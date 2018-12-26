#a) Write a python program to implement the following :
#Given an array of length 3, return an array with the elements "rotated left" so that
#{1, 2, 3} yields {2, 3, 1}.
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
