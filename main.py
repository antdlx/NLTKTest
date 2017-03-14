#-*- coding:utf-8 -*-

import IOFunctions
import Pretreatment


ioFunctions = IOFunctions.IOFunctions()
pretreatment = Pretreatment.Pretreatment()

raw = ioFunctions.ReadFile('D:\\codes\\Python\\PythonSpace\\NLTKTest\\articles.txt')
sents = pretreatment.SenToken(raw)
cleanSents  = pretreatment.CleanSents(sents)
words = pretreatment.WordToken(cleanSents)
stemWords = pretreatment.StemWords(words)
tagged_words = pretreatment.TagWords(stemWords)
# chunked_words = pretreatment.ChunkWords(tagged_words)
# iob = pretreatment.IOBTree(chunked_words)

#将处理完的语料保存到output文件中去
file = open("output.txt","w")
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
