f = open('hamlet.txt','r')
search_word = input('what to search?')
#lines = f.readlines()
for line in f:
    if search_word in line:
        print(line)
f.close()
