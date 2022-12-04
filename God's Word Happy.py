import random
str = ""
Filename = open("Happy.txt")
File = Filename.readline()
lst = []
for word in Filename:
    lst.append(word.strip())
for i in range(32):
    num = random.randrange(len(lst)-1)
    str = str + " " + lst[num]
print(str)
Filename.close()
input()
