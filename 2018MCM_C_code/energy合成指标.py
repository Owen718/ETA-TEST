# 可持续发展合成指标
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df


file_path = r'C:\Users\Owen\Documents\2018MCM_C_code\PCA处理结果'

Status = ['AZ','CA','NM','TX']

for s in Status:
    file_path_s = os.path.join(file_path,s) 
    csv_file1 = os.path.join(file_path_s,'Clean_index.csv') 
    csv_file2 = os.path.join(file_path_s,'No_clean_index.csv')
    
    csv_data1 = data_init(csv_file1)
    csv_data2 = data_init(csv_file2)

    Clean_data = csv_data1.data[csv_data1.year == 2009]
    No_clean_data = csv_data2.data[csv_data2.year == 2009]

    Final_energe_index = (Clean_data / (Clean_data+No_clean_data)) * 100    
    Final_energe_index = int(Final_energe_index)
    print(s+':'+str(Final_energe_index))