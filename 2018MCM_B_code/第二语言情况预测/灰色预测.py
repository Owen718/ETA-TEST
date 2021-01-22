import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from graypredictmodel import GrayForecast
import csv
import os


data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\第二语言情况预测\第二语言数据集'
save_path = r'C:\Users\Owen\Documents\2018MCM_B_code\第二语言情况预测\第二语言情况预测结果\\'
file_list = os.listdir(data_path)

if len(file_list) == 0:
    print('目录中没有文件！')
    exit()

for csv_file_name in file_list:
    csv_file = os.path.join(data_path,csv_file_name)

    f= open(csv_file)
    df = pd.read_csv(f)
    objective_years = 55 #50年后
    grayforecast = GrayForecast(df,'total_users')
    grayforecast.forecast(objective_years)
    grayforecast.level_check()


    data_array = [] #预测结果数组
    population = np.array(grayforecast.log())
    years = np.array(range(2015,2055+objective_years+1))


    save_name = save_path + csv_file_name.split('_')[0] + '_predict2015_2070.csv'
    print(csv_file_name.split('_')[0] +' over!')

    with open(save_name,'w+',newline='') as csv_f:  #数据写入
        writer = csv.writer(csv_f,delimiter = ',')
        writer.writerow(['years','L2_users'])
        for i in range(0,objective_years):
            writer.writerow([years[i],population[i][0]])
