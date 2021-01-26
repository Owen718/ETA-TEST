import numpy as np
import pyecharts
import matplotlib.pyplot as plt
import pandas as pd
import csv


file_name = '数据清洗\ProblemCData.xlsx'
#file_name = '数据清洗\test.xlsx'
save_path = r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\按州分\\'

sh = pd.read_excel(file_name,sheet_name = 0)

print(sh)
index_record=[] #遍历记录

index_data = []
start_years = 0
end_years = 0
length = 0

for i,MSN in enumerate(sh.MSN): 
    #print(sh.MSN[i],sh.StateCode[i],sh.Year[i],sh.Data[i])
    index_r = sh.MSN[i]+sh.StateCode[i] #一条数据的标记
    length+=1
    if index_r not in index_record: #一个州的一种指标的历年数据文件未被创建
        index_data.append(sh.Data[i]) #存入数据
        index_record.append(index_r)
        if i > 0: #如果不是第一个
            end_years = sh.Year[i-1] #结束年份
            start_years = end_years - length + 2
            print(index_data)
            last_data = index_data[-1]
            del index_data[-1]

            save_file =save_path+str(sh.StateCode[i-1])+'\\'+str(sh.MSN[i-1])+'_'+str(sh.StateCode[i-1])+'.csv' 
            with open(save_file,'w+',newline='') as csv_w:
                writer = csv.writer(csv_w,delimiter=',')
                writer.writerow(['years','data'])
                for year,data in enumerate(index_data):
                    writer.writerow([str(int(start_years) + year),data])
                    if year == (len(index_data)-1):
                        if (year+start_years) !=  end_years:
                            print('ERROR!')
                        else:
                            print( str(sh.StateCode[i-1]) +'_'+str(sh.MSN[i-1])+' finish!')

            


            index_data = []
            index_data.append(last_data)
            start_years = 0
            end_years = 0
            length = 1

        
            
            #数据写入



    else:  #一个州的一种指标的历年数据文件已被创建
        index_data.append(sh.Data[i]) #存入数据
    
    
