# -*- coding:utf-8 -*- 

import struct

file1 = open("602080.txt",'rb')
file2 = open("612080.txt",'rb')
num0=[]
num1=[]
num2=[]
num_temp=[]
num1_change=[]
pos=file1.tell()
print pos

def copyarr(arr1,arr2):
    for x in arr2:
        arr1.append(x)

def updataarr(arr1,arr2):
    i=0
    for x in arr2:
        arr1[i]=arr2[i]
        i=i+1

while pos!=0x10000:
    num_tupl=struct.unpack('<I',file1.read(4))
    num=num_tupl[0]
    num1.append(num)
    pos=file1.tell()

pos=file2.tell()
while pos!=0x10000:
    num_tupl=struct.unpack('<I',file2.read(4))
    num=num_tupl[0]
    num2.append(num)
    pos=file2.tell()


copyarr(num_temp,num1)
copyarr(num1_change,num1)

i=0
for x in range(0x4000):
    num0.append(x)           #三个数组创建完成
'''
for n in range(129):
    for x in num_temp:
        num1_change[i]=num_temp[x]
        i+=1
        #print ("0x%x") % temp
    i=0
    updataarr(num_temp,num1_change)
    print num1_change[0],num1_change[1],num1_change[2],num1_change[3],"-------->",n

    //从部分数据看出每位的数据存在循环规律
'''

