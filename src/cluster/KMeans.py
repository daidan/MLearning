# -*- coding: utf-8 -*-
'''
Created on 2016-3-22

@author: dd
'''


from numpy import *
import sys
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import dataPro.DataProcessing as data


#配置UTF-8输出环境
#reload(sys)
#sys.s('utf-8')

k=4
dataSet=data.file2matrix("../file/train_corpus/4k2_far.txt","\t")
dataMat=mat(dataSet[:,1:])  #转换为矩阵形式
print shape(dataMat)

#执行KMeans算法
kmeans=KMeans(init='k-means++',n_clusters=4)

#print [[r[col] for r in dataMat] for col in range(len(dataMat[0]))]  

kmeans.fit(dataMat)
#绘制计算结果的图形
plt.scatter(dataMat,size=20,color='b',mrkr='.')
plt.scatter(kmeans.cluster_centers_,size=60,color='red',mrkr='D')
plt.show()






