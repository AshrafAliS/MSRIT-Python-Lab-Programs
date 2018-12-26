#Write a python function called is_abecedarian that returns True if the letters in a word appear
#in alphabetical order (double letters are ok). How many abecedarian words are there?

def is_abecedarian(word):
    print(''.join(sorted(word)))
    return(word==''.join(sorted(word)))
file = open('words.txt','w+')
file.write(input("Enter some words please: "))

file.close()
with open('words.txt','r+') as file:
    count=0
    for line in file:
        for word in line.split():
            if is_abecedarian(word):
                count +=1
    print("There are",count,"Abecedarian words")
#BEFORE SORTING  AND AFTER SORTING BOTH SHOULD BE SAME
