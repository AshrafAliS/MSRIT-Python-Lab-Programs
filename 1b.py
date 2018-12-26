#Write a python function stats() that takes name of text file as an argument. The function
#should print the number of lines, words, and characters in the file. For example,
#>>>stats('example.txt')
#Line count: 3
#Word count: 20
#Character count: 98
def stat(txt):
    num_lines = 0
    num_words = 0
    num_chars = 0
    with open(txt, 'r') as f:
        for x in f.readlines():
            words = x.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(x)-1
        print("Line count:",num_lines)
        print("Word count:",num_words)
        print("Character count:",num_chars)
stat("2.1a.py")
