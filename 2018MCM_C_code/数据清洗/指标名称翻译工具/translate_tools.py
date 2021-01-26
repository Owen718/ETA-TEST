# -*- coding:utf-8 -*-
import requests
import json
import csv
import pandas as pd
import numpy as np

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

def translate(string):
    data = {
    'doctype': 'json',
    'type': 'AUTO',
    'i':string
    }
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url,params=data)
    result = r.json()
    result = ((result['translateResult'][0])[0])['tgt']
    return result

completed_index_file = r'C:\Users\Owen\Documents\2018MCM_C_code\各州各指标完整性\completed-index.csv'
index_description_file = r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\指标名称翻译工具\index.csv'

completed_csv = data_init(completed_index_file)
index_description_csv = data_init(index_description_file)

MSN_list = []
result_list = []

for i,c_index in enumerate(completed_csv.MSN): #筛出完整度指标最高的指标
    if round(completed_csv.completed_index[i],1) == 3.4 : #指标为最高值
        translate_str = str(np.array(index_description_csv[index_description_csv.MSN == c_index].Description)[0])
        translate_result = translate(translate_str)
        print(translate_result)
        result_list.append(translate_result)
        MSN_list.append(c_index) 

save_file = 'Chinese-index.csv'
with open(save_file,'w+',newline='') as csv_w:
    writer = csv.writer(csv_w,delimiter=',')
    writer.writerow(['MSN','Desctription'])
    for i,data in enumerate(result_list):
        writer.writerow([MSN_list[i],result_list[i]])
        print(str(MSN_list[i])+' completed-index finished!')   