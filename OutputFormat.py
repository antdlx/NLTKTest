#-*- coding:utf-8 -*-

class ClassOutputFormat:
    def doFormat(self):
        file1 = open("output_result.txt")
        result = list()
        sen = list()
        word = list()
        word_num = 0
        jump = False
        LOC = "I-LOC"

        for line in file1:
            line = line.split()
            word = []
            if len(line) == 0:
                result.append(sen)
                sen = []
                word_num = 0
                continue

            if line[4] == LOC:
                word.append(word_num)
                word.append(line[0])
                sen.append(word)
            word_num += 1

        print(result)

        #合并2个相连的地理词

        for s in result:
            num = len(s)
            if num >= 2:
                for w in range(0,num-1):
                    index = s[w+1][0]-s[w][0]
                    if index == 1:
                        s[w][1] += (" "+s[w+1][1])
                        s[w][0] = s[w+1][0]
                        del s[w+1]
                        num -= 1

        print(result)
        return result