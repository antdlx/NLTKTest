#-*- coding:utf-8 -*-
#统计地理词后缀

file1 = open("affixs.txt")

affixs = dict()

for line in file1:
    affixs[line[:-1]]=1


file2 = open("outputAffix","w")
file3 = open("outputBig.txt")
#先清空以前的
file2.truncate()
file3.seek(0)
for line in file3:
    string = ""
    mlist = line.split()
    if len(mlist) == 0:
        string += "\n"
        file2.write(string)
        continue

    if len(mlist[0])>=3:
        if affixs.has_key(mlist[0][-3:].lower())==True:
            mlist.append("G")
        else:
            mlist.append("O")
    else:
        mlist.append("O")

    for word in mlist:
        string += word +" "
    string+="\n"
    file2.write(string)

# print("els is {0},ine is {1},the is {2}".format(affixs['els'],affixs['ine'],affixs['the']))
file2.close()
print("length is {0}".format(len(affixs)))