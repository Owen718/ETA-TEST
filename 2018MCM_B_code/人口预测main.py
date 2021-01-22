import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from graypredictmodel import GrayForecast
import csv

f = open(r'C:\Users\Owen\Documents\2018MCM_B_code\2010-2020人口数据\')
df = pd.read_csv(f)
file_name = 'Russia_predict_2010_2060.csv'
#print(df.years,df.money)
objective_years = 50 #50年后


grayforecast = GrayForecast(df,'population')
grayforecast.forecast(objective_years)


data_array = [] #预测结果数组
population = np.array(grayforecast.log())
years = np.array(range(2010,2010+objective_years+1))

with open(file_name,'w+',newline='') as csv_f:  #数据写入
    writer = csv.writer(csv_f,delimiter = ',')
    writer.writerow(['years','population'])
    for i in range(0,len(years)):
        writer.writerow([years[i],population[i][0]])
