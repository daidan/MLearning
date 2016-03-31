# -*- coding: utf-8 -*-
'''
Created on 2016年3月22日

@author: daidan
'''
import sys
import os
import jieba

from sklearn.datasets.base import Bunch  #引入Bunch类
import pickle

#配置UTF-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

#保存至文件
def savefile(savepath,content):
    fp=open(savepath,"wb")
    fp.write(content)
    fp.close()
    
    
    #读取文件
def readfile(path):
    fp=open(path,"rb")
    content=fp.read()
    fp.close()
    return content


corpus_path="../file/test_corpus/"  #未分词语料库路径
seg_path="../file/train_corpus/"    #分词后的分类语料库路径

catelist = os.listdir(corpus_path)

#获取每个目录下的所有文件
for mydir in catelist:  #获取corpus_path下的所有子目录
    class_path=corpus_path+mydir+"/"  #拼出分类子目录的路径
    seg_dir=seg_path+mydir+"/"   #拼出分词后的语料分类目录
    if not os.path.exists(seg_dir): #是否存在目录，如果没有则创建
        os.mkdir(seg_dir)
        #os.makedirs(seg_dir)
    file_list=os.listdir(class_path)   #获取类别目录下的所有文件
    for file_path in file_list:  #遍历类别目录下的文件
     fullname=class_path+file_path #拼出文件名全路径
     content=readfile(fullname).strip()  #读取文件内容
     content=content.replace("\r\n","").strip() #删除换行和多余的空格
     content_seg=jieba.cut(content)  #为文件内容分词
     #将处理后的文件保存到分词后语料目录
     savefile(seg_dir+file_path," ".join(content_seg))
     
print "中文语料分词结束！"   
     
     
     
'''
Bunch类提供一种key、value的对象形式
target_name 所有分类集名称列表
label 每个文件的分类标签列表
filenames 文件路径
contents 分词后文件词向量形式
'''
bunch=Bunch(target_name=[],label=[],filenames=[],contents=[])        
wordbag_path="../file/train_word_bag/train_set.dat" #分词语料Bunch对象持久化
seg_path="../file/train_corpus_seg/"     #分词后分类语料库路径
 
catelist=os.listdir(seg_path)
bunch.target_name.extend(catelist)  #将类别信息保存到Bunch对象中
for mydir in catelist:
    class_path=seg_path+mydir+"/"
    file_list=os.listdir(class_path)
    for file_path in file_list:
        fullname=class_path+file_path
        bunch.label.append(mydir)   #保存当前文件的分类标签
        bunch.filenames.append(fullname) #保存当前文件的文件路径
        bunch.content.append(readfile(fullname).strip()) #保存文件词向量
        
#bunch对象持久化
file_obj=open(wordbag_path,"wb")
pickle.dump(bunch,file_obj)
file_obj.close();



print "构建文本对象接受！"
        
    





    
    