#-*- coding:utf-8 -*-
#找出geo_text文件中长度大于1的地理词组
import re
class TwoThreeWord:
    #最少出现次数
    BUTTOM = 3
    def do23word(self):
        file1 = open("geo_test.txt")
        line_num = 0
        ttwords=dict()

        for line in file1:
            line_num += 1
            if line_num == 1 or line_num%3==0:
                line = re.sub("\[","",line)
                line = re.sub("\]","",line)
                line = re.sub("[0-9]","",line)
                # line = re.sub(",","",line)
                line = re.sub("u'","",line)
                line = re.sub("\'","",line)

                line = line.split(",")
                # print(line)
                if len(line)>0 and line[0] != "MONGODB ERROR: (__init__) geography\n":
                    for word in line:
                        if len(word.split()) > 1:
                            if ttwords.has_key(word)==False:
                                ttwords[word] = 1
                            else:
                                ttwords[word] += 1
        return ttwords

ttw = TwoThreeWord()
result=ttw.do23word()
keys = result.keys()

file1 = open("23words.txt","w")
file1.truncate()
string = ""
for k in keys:
    if result[k] > ttw.BUTTOM:
        string += k + "\n"
file1.write(string)
file1.close()