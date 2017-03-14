#-*- coding:utf-8 -*-
import  sys

#从命令行获取文件参数构建路径
path = sys.argv[0]+"\\..\\"+sys.argv[1]
# print(path)
# file = open('eng1test_info.txt')
file = open(path)
# line = file.readline()

#初始化训练集中真正为4种类型的词的数量
num_per = 0.0
num_org=0.0
num_loc=0.0
num_misc=0.0
#初始化模型预测的4种类型的词的数量
p_num_per=0.0
p_num_org=0.0
p_num_loc=0.0
p_num_misc=0.0
#初始化预测对的4种类型的词的数量
t_num_per=0.0
t_num_org=0.0
t_num_loc=0.0
t_num_misc=0.0

#初始化字符串
PER="I-PER"
ORG="I-ORG"
LOC="I-LOC"
MISC="I-MISC"

for line in file:
    list = line.split()
    #用于跳过空行
    if len(list)==0:
        continue

    #如果预测正确
    if list[3]==list[4]:
        if list[3]==PER:
            num_per += 1
            p_num_per += 1
            t_num_per +=1
        if list[3]==ORG:
            num_org += 1
            p_num_org += 1
            t_num_org += 1
        if list[3]==LOC:
            num_loc += 1
            p_num_loc += 1
            t_num_loc += 1
        if list[3]==MISC:
            num_misc += 1
            p_num_misc += 1
            t_num_misc += 1
    #如果预测错误
    else:
        if list[3]==PER:
            num_per += 1
        if list[3]==ORG:
            num_org += 1
        if list[3]==LOC:
            num_loc += 1
        if list[3]==MISC:
            num_misc += 1
        if list[4]==PER:
            p_num_per += 1
        if list[4]==ORG:
            p_num_org += 1
        if list[4]==LOC:
            p_num_loc += 1
        if list[4]==MISC:
            p_num_misc += 1

    # line = file.readline()

    # file.close()

print ("共有PER: {0} ;统计正确: {1} ;预测有: {2}\n".format(num_per,t_num_per,p_num_per))
print ("共有ORG: {0} ;统计正确: {1} ;预测有: {2}\n".format(num_org,t_num_org,p_num_org))
print ("共有LOC: {0} ;统计正确: {1} ;预测有: {2}\n".format(num_loc,t_num_loc,p_num_loc))
print ("共有MISC: {0} ;统计正确: {1} ;预测有: {2}\n".format(num_misc,t_num_misc,p_num_misc))

#初始化4种类型的P值
per_p = 0.0
org_p = 0.0
loc_p = 0.0
misc_p = 0.0
#初始化4种类型的R值
per_r = 0.0
org_r = 0.0
loc_r = 0.0
misc_r = 0.0
#初始化4种类型的F值
per_f = 0.0
org_f = 0.0
loc_f = 0.0
misc_f = 0.0

if p_num_per !=0:
    per_p = t_num_per/p_num_per
if p_num_org !=0:
    org_p = t_num_org/p_num_org
if p_num_loc !=0:
    loc_p = t_num_loc/p_num_loc
if p_num_misc !=0:
    misc_p = t_num_misc/p_num_misc

if num_per !=0:
    per_r = t_num_per/num_per
if num_org !=0:
    org_r = t_num_org/num_org
if num_loc !=0:
    loc_r = t_num_loc/num_loc
if num_misc !=0:
    misc_r = t_num_misc/num_misc

if (per_r+per_p)>0:
    per_f = 2*per_p*per_r/(per_p+per_r)
if (org_r+org_p)>0:
    org_f = 2*org_p*org_r/(org_p+org_r)
if (loc_p+loc_r)>0:
    loc_f = 2*loc_p*loc_r/(loc_p+loc_r)
if (misc_p+misc_r)>0:
    misc_f = 2*misc_r*misc_p/(misc_r+misc_p)

print("PER的P值为：{0}% ;R值为：{1}% ;F值为：{2}%\n".format(per_p*100,per_r*100,per_f*100))
print("ORG的P值为：{0}% ;R值为：{1}% ;F值为：{2}%\n".format(org_p*100,org_r*100,org_f*100))
print("LOC的P值为：{0}% ;R值为：{1}% ;F值为：{2}%\n".format(loc_p*100,loc_r*100,loc_f*100))
print("MISC的P值为：{0}% ;R值为：{1}% ;F值为：{2}%\n".format(misc_p*100,misc_r*100,misc_f*100))