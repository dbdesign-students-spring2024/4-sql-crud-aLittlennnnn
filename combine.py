f1 = open('./data/messages.csv','r')
lines1 = f1.readlines()
f2 = open('./data/stories.csv','r')
lines2 = f2.readlines()
lines3 = []

for j in range(len(lines2)-1):
    word = lines2[j+1].split(",")
    # print(word)
    nline = ""
    for i in range(len(word)):
        if i == 0:
            nline += str(int(word[i]) + 1000) + ","
        elif i != len(word)-1:
            nline += str(word[i]) + ","
        else:
            nline += str(word[i])
    lines3.append(nline)

newlines = lines1
for i in range(len(lines3)):
    newlines.append(lines3[i])
    

f3 = open('./data/posts.csv','w')
for line in newlines:
    f3.write(line)