#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:30:46 2019

@author: chengxueping
"""


import csv
def get_class_label_1(number):
    k=0
    num=int(number)
    if num<9:
        pass
    elif num<16:
        k=1
    else:
        k=2
    
    return str(k)

def get_class_label_2(number):
    k=0
    num=int(number)
    if num<7:
        pass
    elif num<9:
        k=1
    elif num<13:
        k=2
    elif num<14:
        k=3
    elif num<16:
        k=4
    elif num<18:
        k=5
    elif num<21:
        k=6
    elif num<23:
        k=7
    elif num<25:
        k=8
    else:
        k=9
    
    return str(k)


L1=[]
L2=[]
L3=[]
file_path='/home/chengxueping/Desktop/competition/Cloud_recognition/Train_label.csv'
with open(file_path) as cf:
    lines=csv.reader(cf)   
    for index,i in enumerate(lines):
        if index==0:
            i.append('label_1')
            i.append('label_2')
            headers=i
        else:
            num=i[1]
            if len(num.split(';'))>1:          
                for ind,j in enumerate(num.split(';')):
                    a=get_class_label_1(j)
                    b=get_class_label_2(j)
        #            print(a)
                    L1.append(a)
                    L2.append(b)
                    if ind != len(num.split(';'))-1:
                        L1.append(';')
                        L2.append(';')
                    else:
                        pass
                com=''.join(L1)
                dom=''.join(L2)
                i.append(com)
                i.append(dom)
                L1=[]
                L2=[]
            else:
                com=get_class_label_1(num)
                dom=get_class_label_2(num)
                i.append(com)
                i.append(dom)
        L3.append(i)
        print('file is :{name},label_1 is {l1},label_2 is {l2}'.format(name=i[0],l1=i[2],l2=i[3]))

#    break  
    
    
f=open('/home/chengxueping/Desktop/competition/Cloud_recognition/translation.csv','a+')
wf=csv.writer(f)
wf.writerow(headers)
wf.writerows(L3[1:])
f.close()
