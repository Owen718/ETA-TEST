import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from graypredictmodel import GrayForecast
import csv
import os

#author: JMU Yetian/Owen
#time: 2021/1/21

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

def get_data(csv_data,language,data_type,years): #传入csv数据 和 language对应的位置信息 返回对应年份的相应数据
    if data_type == 'total':
        data = csv_data[csv_data.Language == language].Total
    if data_type == 'L2 speakers':
        data = np.array(csv_data[csv_data.Language == language])[0][6]
    try:
        return float(data)
    except TypeError:
        print('Error!years:')
        print(years)
        print(language)
        return 0
    



file_path = r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况'
file_list = os.listdir(file_path)  


data_2015 = data_init(r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况\2015.csv')
data_2017 = data_init(r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况\2017.csv')
data_2018 = data_init(r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况\2018.csv')
data_2019 = data_init(r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况\2019.csv') 
data_2020 = data_init(r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况\2020.csv')
save_path = r"C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况\contry\\"
for language in data_2018.Language:
    #total_data_2015 =  #language对应的2015年总使用人数情况
    total_data_2015 = get_data(data_2015,language,'total',2015)
    total_data_2017 = get_data(data_2017,language,'total',2017)
    total_data_2018 = get_data(data_2018,language,'total',2018)
    total_data_2019 = get_data(data_2019,language,'total',2019)
    total_data_2020 = get_data(data_2020,language,'total',2020)
 
    
    with open( save_path + language+'_total.csv','w+',newline='') as csv_w: #数据流重写入
        writer = csv.writer(csv_w,delimiter = ',')
        writer.writerow(['years','total_users'])
        writer.writerow(['2015',total_data_2015])    
        writer.writerow(['2016',(total_data_2015+total_data_2017)/2])
        writer.writerow(['2017',total_data_2017])
        writer.writerow(['2018',total_data_2018])
        writer.writerow(['2019',total_data_2019])
        writer.writerow(['2020',total_data_2020])





