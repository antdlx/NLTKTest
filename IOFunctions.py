#-*- coding:utf-8 -*-
class IOFunctions:
    '用于IO的类'
    def ReadFile(self,filepath):
        f = open(filepath)
        raw = f.read()
        return raw

