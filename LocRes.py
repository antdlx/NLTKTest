#-*- coding:utf-8 -*-

#这个文件是用来处理初始的带有4种分类的语料，将其处理的只剩下I-LOC这一种

file1 = open("eng.testb")
file2 = open("engLoc.testb","w")

for line in file1:
    list = line.split()
    string = ""
    #在不是空行的情况下
    if len(list)!=0:
        if list[3] != "I-LOC":
            list[3] = "O"
        for word in list:
            string+=word+" "
    string += "\n"
    file2.write(string)

file2.close()