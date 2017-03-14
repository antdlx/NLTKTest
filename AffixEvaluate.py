#-*- coding:utf-8 -*-#-*- coding:utf-8 -*-
import  sys

#从命令行获取文件参数构建路径
path = sys.argv[0]+"\\..\\"+sys.argv[1]
# print(path)
# file = open('eng1test_info.txt')
file = open(path)
# line = file.readline()


true_pos=0.0
false_pos=0.0
false_neg=0.0
loc_num=0.0

p=0.0
r=0.0
f=0.0

#初始化字符串
LOC="I-LOC"
O="O"

for line in file:
    list = line.split()
    #用于跳过空行
    if len(list)==0:
        continue

    #如果预测正确
    if list[4]==list[5]:
        if list[4]==LOC:
            true_pos += 1
            loc_num += 1
    #如果预测错误
    else:
        if list[4]==LOC:
            false_neg += 1
            loc_num += 1
        if list[4]==O:
            false_pos += 1

    # line = file.readline()

    # file.close()


print ("共有LOC: {0} ;true_pos: {1} ;false_pos: {2} ;false_neg: {3}\n".format(loc_num,true_pos,false_pos,false_neg))

if (true_pos+false_pos)!=0:
    p = true_pos/(true_pos+false_pos)
if (true_pos+false_neg)!=0:
    r = true_pos/(true_pos+false_neg)
if (p+r)!=0:
    f=2*p*r/(p+r)

print("LOC的P值为：{0}% ;R值为：{1}% ;F值为：{2}%\n".format(p*100,r*100,f*100))