import numpy as np
import pyecharts
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np
import os

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

def compute_data_completeness(csv_file): #计算一个文件的完整性指标
    length = len(np.array(csv_file.years)) #数据跨越度-年
    No_zeros = length - np.sum(np.array(csv_data.data==0).astype(np.uint8)) 
    completed_index = 0.3 * length/100 + 0.7 * (No_zeros)/length
    return completed_index

def compute_data_completeness2(csv_file): #计算一个文件的完整性指标2
    zeros = np.sum(np.array(csv_data.data==0).astype(np.uint8))  #数据为0的情况
    return zeros

def return_msn_list_index(list,index_name): #求指标名对应的矩阵索引
    return list.index(index_name)


file_path = r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\按州分\\'


index_list = []
MSN_list = []

AZ_file_path = file_path +'AZ'
file_list = os.listdir(AZ_file_path)

for file_name in file_list:
    csv_file  = os.path.join(AZ_file_path,file_name)
    csv_data = data_init(csv_file) 
    completed_index = compute_data_completeness(csv_data) #完整性指标
    index_list.append(completed_index)
    MSN_list.append(file_name.split('_')[0])
S = ['CA','NM','TX']

for status in S:
    status_file = os.path.join(file_path+status,file_path)
    for file_name in file_list:
        csv_file  = os.path.join(AZ_file_path,file_name)
        csv_data = data_init(csv_file) 
        completed_index = compute_data_completeness(csv_data) #完整性指标
        msn_index = return_msn_list_index(MSN_list,file_name.split('_')[0])
        index_list[msn_index] += completed_index

    
save_file = 'completed-index.csv'
with open(save_file,'w+',newline='') as csv_w:
    writer = csv.writer(csv_w,delimiter=',')
    writer.writerow(['MSN','completed_index'])
    for i,data in enumerate(index_list):
        writer.writerow([MSN_list[i],index_list[i]])
        print(str(MSN_list[i])+' completed-index finished!')