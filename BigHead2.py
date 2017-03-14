#-*- coding:utf-8 -*-
#将语料进行处理，添加上一列非句首词的大写首字母作为新的特征

class ClassBigHead2:
    def doBigHead2(self):
        file = open("output.txt")
        file2 = open("outputBighead.txt","w")
        file2.truncate()
        line_num = 0
        isHead = False

        for line in file:
            string = ""
            line_num +=1
            wlist = line.split()
            if line_num == 1 or len(wlist) == 0:
                isHead = True
            if len(wlist) == 0:
                string += "\n"
                file2.write(string)
                continue

            words = list(wlist[0])
            if words[0].isupper() and isHead==False:
                wlist.append(words[0])
            else:
                wlist.append("o")
            if len(wlist) != 0:
                isHead = False
            for s in wlist:
                string += s+" "
            string += "\n"
            file2.write(string)

        file2.close()