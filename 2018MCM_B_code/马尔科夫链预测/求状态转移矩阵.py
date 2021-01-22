import numpy as np
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt

def get_P(Y1,Y2): #Y1 Y2 列为每年的数据情况，行为各个国家的情况
    # Y1_determinant = np.linalg.det(Y1)#求解Y1行列式的值
    # Y2_determinant = np.linalg.det(Y2)#求解Y1行列式的值

    Y1_T = Y1.T


    print('Y1.T * Y1:')
    print(np.dot(Y1_T,Y1)) # (Y1.T * Y1) 
    
    #判断矩阵是否可逆
    temp = np.dot(Y1_T,Y1)
    temp_det = np.linalg.det(temp) #temp矩阵行列式的值
    if(temp_det<=0):
        print('错误！矩阵不可逆！')
      
    
    #p_negative = np.linalg.inv(np.dot(Y1_T,Y1))


    #p = np.dot(p,Y2)
    p = np.dot(np.dot(np.linalg.inv(np.dot(Y1.T, Y1)), Y1.T), Y2)
    print('状态转移矩阵：')
    print(p)
    return p

def data_init(csv_file): #读取一个国家的历年情况，并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

# Y_2020
# Y_2021 = P * Y_2020
# Y_2022 = P * Y_2021
# ....

# Y_2020+n = (p * Y_2020)^n


file_path = r'C:\Users\Owen\Documents\2018MCM_B_code\test5contry'
file_list = os.listdir(file_path)


data = []
data_allyears=[]
contry_list = []
for i,file_name in  enumerate(file_list):
    csv_data = data_init(os.path.join(file_path,file_name))
    population_array = np.array(csv_data.population)
    population_all_array = np.array(csv_data.population)


    contry_list.append(file_name)
    data.append(population_array)
    data_allyears.append(population_all_array)

data = np.array(data)
Y1 = np.delete(data,len(population_array)-1,axis=1)
Y2 = np.delete(data,0,axis=1)

Y1 = Y1.T #转变为每一列为一个国家
Y2 = Y2.T #转变为每一列为一个国家

iterate = 10 #迭代次数，也就是预测到 iterat年后
n_features = len(contry_list) #国家数
start_years = 2020 #起始迭代的年份
st = np.zeros((iterate + 1 ,n_features))
p = get_P(Y1,Y2) #获得状态转移矩阵


start_array=[]
for i in range(len(contry_list)):
    start_array.append(data_allyears[i][len(contry_list)])


st[0] = np.array(start_array) #起始迭代的矩阵st0

for i in range(iterate): #迭代运算
    st[i+1] = np.dot(st[i],p) 

# for i in range(iterate+1):
#     st[i] /= np.sum(st[i])

x = range(2020,2020+iterate+1) #x轴

st /= 1000000
for j in range(n_features): #绘图
   plt.plot(x,st.T[j],label = contry_list[j])

plt.legend(loc = 0)
plt.show()