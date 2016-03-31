# -*- coding: utf-8 -*-
'''
Created on 2016年3月22日

@author: daidan
'''
import sys
import os
from sklearn.datasets.base import Bunch  #引入Bunch类
import cPickle as pickle               #引入持久化类
from sklearn import feature_extraction
from sklearn.feature_extraction.text import  TfidfTransformer  #tf-idf向量转换类
from sklearn.feature_extraction.text import  TfidfVectorizer   #tf-idf向量生成类
import WordSeg as wordSeg

#配置UTF-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

#读取Bunch对象
def readbunchobj(path):
    file_obj=open(path,"rb")  #r表示只读,b表示二进制  与此对应的是w表示可写，t表示文本方式打开
    bunch=pickle.load(file_obj)
    file_obj.close()
    return bunch



#写入bunch对象
def writebunchobj(path,bunchobj):
    file_obj=open(path,"rb")
    pickle.dump(bunchobj, file_obj, protocol=0)
    file_obj.close()
    

 #导入分词后的词向量Bunch对象
path="../file/train_word_bag/train_set.dat"    #词向量保存路径
bunch = readbunchobj(path)
 #构建tf-idf词向量空间对象
tfidfspace=Bunch(target_name=bunch.target_name,label=bunch.label,filenames=bunch.filenames,tdm=[],vocabulary={})
 
 #停用词表
stopword_path="../file/train_word_bag/stoplist.txt"
stpwrdlst=wordSeg.readfile(stopword_path).splitlines()
 
 
 
 #使用tfidfVectorizer初始化向量空间模型
 
vectorizer=TfidfVectorizer(stop_words=stpwrdlst,sublinear_tf=True,max_df=0.5)
transformer=TfidfTransformer()  #该类会统计每个词语的tf-idf权值
 #文本转为词频矩阵，单独保存字典文件
tfidfspace.tdm=vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary=vectorizer.vocabulary_
 
 #创建词袋的持久化 
space_path="../file/train_word_bag/tfidfspace.dat"  #词向量词袋保持路径
writebunchobj(space_path,tfidfspace)
 
 
 
    

