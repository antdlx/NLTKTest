#-*- coding:utf-8 -*-

import IOFunctions
import Pretreatment
import re

class ClassMain:
    def doMain(self):
        ioFunctions = IOFunctions.IOFunctions()
        pretreatment = Pretreatment.Pretreatment()

        raw = ioFunctions.ReadFile('D:\\codes\\Python\\PythonSpace\\NLTKTest\\datas\\articles.txt')
        #清除Unicode标签u"和u'
        raw = re.sub("u\"","",raw)
        raw = re.sub("u\'","",raw)
        
        sents = pretreatment.SenToken(raw)
        cleanSents  = pretreatment.CleanSents(sents)
        words = pretreatment.WordToken(cleanSents)
        stemWords = pretreatment.StemWords(words)
        tagged_words = pretreatment.TagWords(stemWords)
        # chunked_words = pretreatment.ChunkWords(tagged_words)
        # iob = pretreatment.IOBTree(chunked_words)

        #将处理完的语料保存到output文件中去
        file = open("datas\\output.txt","w")
        file.truncate()
        for line in tagged_words:
            string=""
            for mtuple in line:
                for word in mtuple:
                    string += word+" "
                string+="\n"
            string+="\n"
            file.write(string)

        file.close()


