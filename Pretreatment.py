#-*- coding:utf-8 -*-
import nltk
import string

from nltk.corpus import wordnet as wn


class Pretreatment:
    '语言预处理的类'
    #将文本分割成句子
    def SenToken(self,raw):
         # sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
         sents = nltk.sent_tokenize(raw)
         return  sents

    #句子内容清理，去掉标点符号、数字和非字母字符
    def CleanSents(self,sents):
         cleanSents = []
         identify = string.maketrans('', '')
         delEStr = string.punctuation +string.digits  #ASCII 标点符号，数字
         for sent in sents:
             cleanSents.append(sent.translate(identify,delEStr)) #去掉ASCII 标点符号
         return cleanSents

    #进行词干化，使用Wordnet
    def StemWords(self,cleanWordsList):
        stemWords=[]
        for words in cleanWordsList:
            line=[]
            for word in words:
                tmp=wn.morphy(word)
                if tmp == None:
                    line.append(word)
                else:
                    line.append(tmp)
            stemWords.append(line)
        return stemWords

    #将句子分割成单词
    def WordToken(self,sents):
        words = []
        for sent in sents:
            words.append(nltk.word_tokenize(sent))
        return words

    #对单词进行POS标记
    def TagWords(self,words):
        tagged = []
        for word in words:
            tagged.append(nltk.pos_tag(word))
        return tagged

    #对已经POS过的词进行chunk
    def ChunkWords(self,tagged):
        entities=[]
        for tag in tagged:
            # entities.append(nltk.ne_chunk(tag))
            entities.append(nltk.conllstr2tree(tag,chunk_types=('NP', 'PP', 'VP'), root_label='S'))
        return entities

    def IOBTree(self,trees):
        iob=[]
        for tree in trees:
            iob.append(nltk.tree2conlltags(tree))
        return iob