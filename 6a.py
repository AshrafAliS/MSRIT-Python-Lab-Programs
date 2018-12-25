#(a)	Write a python program to read lines of input from the user, without giving a prompt. When the input line is quit, stop accepting input. As output, print the input lines in reverse order, one on each output line. The line quit should not be included in the output. Do not use the Python list reverse method.Sample input and outputs are
##Input :   hello world cse 326 32.545 ostrich quit 
#Output: ostrich 32.545 326 cse hello world
linelist=list()
while True:
    line=input()
    if line=='quit':
        break
    else:
        linelist.append(line)
for i in range(len(linelist)-1,-1,-1):
    print(linelist[i])
