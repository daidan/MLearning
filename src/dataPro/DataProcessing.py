# -*- coding: utf-8 -*-
'''
Created on 2016年3月22日

@author: daidan
'''
import sys
import os
from numpy import *


#配置UTF-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

#数据文件转矩阵
def file2matrix(path,delimiter):
    #path 数据文件路径  delimiter 行内字段分隔符
    recordlist=[]
    fp=open(path,"rb")   #读取文件内容
    content=fp.read()
    fp.close()
    
    rowlist=content.splitlines() #按行转换为一维表
    #逐行遍历，结果按分割符分隔为行向量
    
    recordlist=[row.split()  for row in rowlist if row.strip()]
    return mat(recordlist) #返回转换后的矩阵形式

'''
root="../file/train_corpus"  #数据文件所在路径
   
pathlist=os.listdir(root) #获取路径下的所有数据文件
for path in pathlist:
    recordmat=file2matrix(root+"/"+path,"\t") #文件到矩阵的转换
    print shape(recordmat) 
 '''   



###############################################################################

