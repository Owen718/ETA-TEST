import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import numpy as np
#data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\test'
#data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\2020-2070年全球主要语言情况预测结果'
data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\第二语言情况预测\第二语言情况预测结果'

file_list = os.listdir(data_path)

if len(file_list) == 0:
    print('目录中没有文件！')
    exit()

plt_data = []
plt.figure(figsize=(10,10))
plt.xlabel('years')
plt.ylabel('L2_users')
for i,csv_file_name in enumerate(file_list):
    label = csv_file_name.split('_') 
    f = open(os.path.join(data_path,csv_file_name ))
    df = pd.read_csv(f)
    population_data = np.array(df.L2_users)
    years_data = np.array(df.years)

    plt.plot(years_data,population_data,label = label[0])

plt.legend(loc=2)
plt.show()
