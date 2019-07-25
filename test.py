# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 09:02:45 2018

@author: dongfang
"""
#引入包
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import xlrd

#实验数据集的引入
file = '2015数据整理 1.2.xlsx'
#file = '2016数据整理 1.2.xlsx'
#file = '2017数据整理 1.2.xlsx'
#file = '2018数据.xlsx'
wb = xlrd.open_workbook(filename=file)
ws = wb.sheet_by_name('2015')

dataset = []#原始数据集
train_data = []#训练特征集合
train_val = []#实际运价指数

for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r,c).value)
    dataset.append(col)
    train_data.append(col[:15])
    train_val.append(col[18])
X = train_data
y = train_val

#data processing
train = 222 #the number of the train data

realData = pd.DataFrame(dataset)

L = len(realData)#the total number of the experimental data
total_predict_data=L-train

#draw
ax=realData.plot()
ax.set_ylabel('Value')

plt.grid(True)
plt.show()

#create data
















