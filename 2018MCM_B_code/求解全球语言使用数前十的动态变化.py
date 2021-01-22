import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import numpy as np
data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\test'
data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\2020-2070年全球主要语言情况预测结果'

def data_sort_st(data_all,year): #按照第year年的情况排序，并返回前十名的语言
    new_data = data_all
    result = sorted(new_data,key = lambda a:a[year-2020+1],reverse=True)

    language_10st = []
    for i in range(0,10,1):
        language_10st.append(result[i][0])
    return language_10st



file_list = os.listdir(data_path)

if len(file_list) == 0:
    print('目录中没有文件！')
    exit()

data_all=[]
one_contry_name = []
for i,csv_file_name in enumerate(file_list):
    label = csv_file_name.split('_') 
    f = open(os.path.join(data_path,csv_file_name ))
    df = pd.read_csv(f)
    totalusers_data = list(df.total_users) #使用总人数
    years_data = np.array(df.years)
    
    one_contry = []

    one_contry.append(csv_file_name.split('_')[0])
    one_contry += totalusers_data
    data_all.append(one_contry)


years = 50
save_name = '全球2020_2070年前十大总使用人数的语言.csv'
with open(save_name,'w+',newline='') as csv_f:
    writer = csv.writer(csv_f,delimiter = ',')
    writer.writerow(['years','Rank1','Rank2','Rank3','Rank4','Rank5','Rank6','Rank7','Rank8','Rank9','Rank10',])
    for i in range(2020,2020+years+1):
        writer.writerow([str(i),data_sort_st(data_all,i)])



