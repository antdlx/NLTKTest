#-*- coding:utf-8 -*-
import re

class ClassOutputFormat:
    def doFormat(self):
        file1 = open("datas\\output_result.txt")
        #二次检查地理词，消耗性能提高准确率
        sec_words = dict()
        LOC = "I-LOC"

        lines = file1.readlines()
        line_num = len(lines)
        #自定义2，构建23词表
        file2 = open("datas\\23words.txt")
        ttwords = dict()
        for fline in file2:
            ttwords[fline[:-1]] = 1

        #从文件中读取并组织成相应的输出结构
        for i in range(0,line_num):
            line = lines[i].split()
            if len(line) == 0:
                continue

            #自定义规则1，查询接下来的2~3词是否在23词表中,为了计算方便，舍弃最后3个词的检测
            #系统对过个单词组成的地理词检测不好，此规则弥补
            if i < line_num-2:
                if len(lines[i+1].split())>0 :
                    tmp = line[0]+" "+lines[i+1].split()[0]
                    if ttwords.has_key(tmp)==True:
                            line[4]=LOC
                            lines[i] = re.sub("\\tO\\n","\\t"+LOC+"\\n",lines[i])
                            lines[i+1] = re.sub("\\tO\\n","\\t"+LOC+"\\n",lines[i+1])
                    if len(lines[i+2].split()) >0:
                        tmp2 = line[0]+" "+lines[i+1].split()[0]+" "+lines[i+2].split()[0]
                        if ttwords.has_key(tmp2)==True:
                            line[4]=LOC
                            lines[i] = re.sub("\\tO\\n","\\t"+LOC+"\\n",lines[i])
                            lines[i+1] = re.sub("\\tO\\n","\\t"+LOC+"\\n",lines[i+1])
                            lines[i+2] = re.sub("\\tO\\n","\\t"+LOC+"\\n",lines[i+2])

            if line[4] == LOC:
                #添加到字典，方便二次查询的时候使用HashMap原理快速查找
                if sec_words.has_key(line[0])==False:
                    sec_words[line[0]]=1

        result = list()
        sen = list()
        word_num = -1

        #自定义规则3：二次检索,只且只需要对一元地理词进行处理即可，可以通过在sec_words词表中添加自定义单词进一步提高准确率
        #添加自定义单词：
        custom = ["London","Mediterranean","Oakland","California","Philippines","Washington","Philippine","Oregon","Nevada",
                  "Washington","Delaware","Manila","Arizona","Colorado","Maine","Massachusetts","Cambridge","Britain","Oxford",
                  "Austria","Alaska"]
        for c in custom:
            if sec_words.has_key(c)==False:
                sec_words[c]=1
        #二次检验
        for line in lines:
            line = line.split()
            word = []
            if len(line) == 0:
                result.append(sen)
                sen = []
                word_num = -1
                continue
            #自定义规则2：在句子前3个单词，且全部为大写的时候，认为是地理词
            #系统对句首全大写地理词识别不好，此规则弥补
            word_num += 1
            if word_num < 3 and line[0].isupper()==True and len(line[0])>=3:
                line[4] = LOC
                # lines[i] = re.sub("\\tO\\n","\\t"+LOC+"\\n",lines[i])
            if sec_words.has_key(line[0])==True:
                line[4]=LOC
            if line[4] == LOC:
                word.append(word_num)
                word.append(line[0])
                sen.append(word)

        #合并2个相连的地理词
        for s in result:
            num = len(s)
            if num >= 2:
                flag = True
                index = 0
                while flag:
                    if s[index+1][0]-s[index][0] == 1:
                        s[index][1] += (" "+s[index+1][1])
                        s[index][0] = s[index+1][0]
                        del s[index+1]
                    else:
                        index += 1
                    if index >= (len(s)-1):
                        flag = False

        file1.close()
        file2.close()
        print(result)
        return result