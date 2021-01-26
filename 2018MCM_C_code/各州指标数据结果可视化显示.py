# -*- coding:utf-8 -*-
import requests
import json
import csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


#csv_file=r'C:\Users\Owen\Documents\2018MCM_C_code\绿色指标.csv'
csv_file=r'C:\Users\Owen\Documents\2018MCM_C_code\非绿色指标.csv'
data_path=r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\按州分'

def max_f(x_array): #隶属函数
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        result_array[i] = x / np.max(x_array)
    return result_array  

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

csv = data_init(csv_file)



Status = ['AZ','CA','NM','TX']

status = Status[3]
plt.figure(figsize=(15,10))
plt.title('the trend of related indices of Non-clean energy in '+status+' from 1960 to 2009')
#plt.title('the trend of related indices of clean energy in '+status+' from 1960 to 2009')
plt.xlabel(u'year',fontsize=14)
plt.ylabel(u'index',fontsize=14)


for MSN in csv.MSN: #11个指标
    csv_f_path = os.path.join(data_path,status)
    csv_f_path += '\\'+MSN + '_' + status +'.csv'
    csv_f = data_init(csv_f_path)
    data = max_f(np.array(csv_f.data))
    plt.plot(np.array(csv_f.years),data,label=MSN)

plt.legend(loc = 2)
plt.show()




        
