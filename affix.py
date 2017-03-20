#-*- coding:utf-8 -*-
#从训练集统计地理词后缀

file1 = open("engLocBighead.train")

affixs = dict()
LOC = "I-LOC"
BUTTOM_LINE=120


for line in file1:
    affix=""
    mlist = line.split()
    if len(mlist) == 0:
        continue
    if mlist[3] == LOC:
        if len(mlist[0])>=3 :
            if affixs.has_key(mlist[0][-3:].lower())==True:
                affixs[mlist[0][-3:].lower()] += 1
            else:
                affixs[mlist[0][-3:].lower()] = 1

keys = affixs.keys()
for k in keys:
    if affixs[k] <= BUTTOM_LINE:
        del affixs[k]

print(affixs)


file2 = open("engLocBigheadAffix.train","w")
#先清空以前的
file2.truncate()
file1.seek(0)
for line in file1:
    string = ""
    mlist = line.split()
    if len(mlist) == 0:
        string += "\n"
        file2.write(string)
        continue

    mlist.append(mlist[3])
    if len(mlist[0])>=3:
        if affixs.has_key(mlist[0][-3:].lower())==True:
            mlist[3] = "G"
        else:
            mlist[3] = "O"
    else:
        mlist[3] = "O"

    for word in mlist:
        string += word +" "
    string+="\n"
    file2.write(string)

# print("els is {0},ine is {1},the is {2}".format(affixs['els'],affixs['ine'],affixs['the']))
file2.close()
print("length is {0}".format(len(affixs)))

file3 = open("affixs.txt","w")
aff = ""
for i in affixs:
    aff += i+"\n"
file3.write(aff)
file3.close()