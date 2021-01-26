# -*- coding:utf-8 -*-
import requests
import json
import csv
import pandas as pd
import numpy as np

csv_file =  r'C:\Users\Owen\Documents\2018MCM_C_code\Chinese-index.csv'
save_file = 'Chinese-index_按单位筛除.csv'

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

csv_f = data_init(csv_file)

string = 'ARCIP'



with open(save_file,'w+',newline='') as csv_w:
    writer = csv.writer(csv_w,delimiter=',')
    writer.writerow(['MSN','Desctription'])
    for i,c_index in enumerate(csv_f.MSN): #筛出完整度指标最高的指标
        if str(c_index)[-1] != 'P':
            writer.writerow([c_index,np.array(csv_f.Desctription)[i]])