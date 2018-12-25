#(a)	Write an interactive python program having a function called Initials() that takes input  representing a full name and returns the initials of the name in all capital letters. For example If Input: Robert B. Qwerty   then Output : RBQ
name = input("Enter Name\t")
def Initials(n):
    initials= ''.join([s[:1].upper() for s in n.split(' ')])
    return initials
print (Initials(name))
