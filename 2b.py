#Write a python function censor() that takes the name of a file as an argument. The function
#should replace every occurrence of a four-letter word in the file with string 'xxxx' and then
#write it into file ‘censored.txt’.
def censor(filename):
    with open(filename,'r+') as f1, open('censor.txt','w+') as f2:
        for line in f1:
            for word in line.split(' '):
                if len(word)==4:
                    print(word)
                    line=line.replace(word,'xxxx')
            f2.write(line)
file=open('samplefile.txt','w+')
file.write('howa aree you men am waitin g fro you')
file.close()
censor('samplefile.txt')
