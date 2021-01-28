# -*- coding:utf-8 -*-
import requests
import json
import csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.decomposition import  PCA

clean_csv_file=r'C:\Users\Owen\Documents\2018MCM_C_code\绿色指标.csv'
No_clean_csv_file=r'C:\Users\Owen\Documents\2018MCM_C_code\非绿色指标.csv'
data_path=r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\按州分'

def normalize_f(x_array): #归一化处理
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        result_array[i] = (x- np.min(x_array) ) / (np.max(x_array) - np.min(x_array))
    return result_array  

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

plt.figure(figsize=(15,10))

clean_csv = data_init(clean_csv_file)
No_clean_csv = data_init(No_clean_csv_file)


Status = ['AZ','CA','NM','TX']

status = Status[0]
clean_data_all = []
No_clean_data_all = []

for MSN in clean_csv.MSN: 
    csv_f_path = os.path.join(data_path,status)
    csv_f_path += '\\'+MSN + '_' + status +'.csv'
    csv_f = data_init(csv_f_path)
    data = normalize_f(np.array(csv_f.data))
    clean_data_all.append(data)

clean_data_all = np.array(clean_data_all).T
clean_data_all = PCA(n_components=1).fit_transform(clean_data_all)

for MSN in No_clean_csv.MSN:
    csv_f_path = os.path.join(data_path,status)
    csv_f_path += '\\'+MSN + '_' + status +'.csv'
    csv_f = data_init(csv_f_path)
    data = normalize_f(np.array(csv_f.data))
    No_clean_data_all.append(data)

No_clean_data_all = np.array(No_clean_data_all).T
No_clean_data_all = PCA(n_components=1).fit_transform(No_clean_data_all)


No_clean_data_all.reshape(50)
clean_data_all.reshape(50)

plt.plot(range(1960,2010),No_clean_data_all,label = 'No-clean energy index in ' + status)
plt.plot(range(1960,2010),clean_data_all,label = 'Clean energy index in ' + status)

plt.legend(loc = 2)
#plt.show()

save_path = r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\PCA处理结果\\'
save_path += status

clean_save_file = os.path.join(save_path,'Clean_index.csv')
No_clean_save_file = os.path.join(save_path,'No_clean_index.csv')

print('')
# with open(clean_save_file,'w+',newline='') as csv_w:
#     writer = csv.writer(csv_w,delimiter=',')
#     writer.writerow(['year','data'])
#     years = range(1960,2010)
#     for i,data in enumerate(clean_data_all):
#         writer.writerow([years[i],clean_data_all[i][0]])

# with open(No_clean_save_file,'w+',newline='') as csv_w:
#     writer = csv.writer(csv_w,delimiter=',')
#     writer.writerow(['year','data'])
#     years = range(1960,2010)
#     for i,data in enumerate(No_clean_data_all):
#         writer.writerow([years[i],No_clean_data_all[i][0]])
    