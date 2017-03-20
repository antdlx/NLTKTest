#-*- coding:utf-8 -*-
#提取数据集的后缀

class ClassAffix2:
    def doAffix2(self):
        file1 = open("datas\\affixs.txt")

        affixs = dict()

        for line in file1:
            affixs[line[:-1]]=1


        file2 = open("datas\\outputAffix.txt","w")
        file3 = open("datas\\outputBighead.txt")
        #先清空以前的
        file2.truncate()
        file3.seek(0)
        for line in file3:
            string = ""
            mlist = line.split()
            if len(mlist) == 0:
                string += "\n"
                file2.write(string)
                continue

            if len(mlist[0])>=3:
                if affixs.has_key(mlist[0][-3:].lower())==True:
                    mlist.append("G")
                else:
                    mlist.append("O")
            else:
                mlist.append("O")

            for word in mlist:
                string += word +" "
            string+="\n"
            file2.write(string)

        # print("els is {0},ine is {1},the is {2}".format(affixs['els'],affixs['ine'],affixs['the']))
        file2.close()
        print("length is {0}".format(len(affixs)))