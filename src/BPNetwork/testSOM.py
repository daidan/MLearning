# -*- coding: utf-8 -*-
'''
Created on 2016年4月7日

@author: daidan
'''
import numpy as np 
from SelfOrgMap import *
from numpy import *
import matplotlib.pyplot as plt 

def errorfunc(inX):
    return sum(power(inX,2))*0.5

SOMNet = SelfOrgMap()
SOMNet.loadDataSet("dataset2.txt");
SOMNet.train()
print SOMNet.w
SOMNet.showCluster(plt)
SOMNet.TrendLine(plt,SOMNet.lratelist)
SOMNet.TrendLine(plt,SOMNet.rlist)