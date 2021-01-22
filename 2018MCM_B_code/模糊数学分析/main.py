import pandas as pd
import numpy as np
RI_dict = {1:0,2:0,3:0.52,4:0.89,5:1.12,6:1.26,7:1.36,8:1.41,9:1.46,10:0.49,11:0.52,12:1.54,13:1.56,14:1.58,15:1.59}

def get_w(array):
    row = array.shape[0]  # 计算出阶数
    a_axis_0_sum = array.sum(axis=0)
    # print(a_axis_0_sum)
    b = array / a_axis_0_sum  # 新的矩阵b
    # print(b)
    b_axis_0_sum = b.sum(axis=0)
    b_axis_1_sum = b.sum(axis=1)  # 每一行的特征向量
    # print(b_axis_1_sum)
    w = b_axis_1_sum / row  # 归一化处理(特征向量)
    nw = w * row
    AW = (w * array).sum(axis=1)
    # print(AW)
    max_max = sum(AW / (row * w))
    # print(max_max)
    CI = (max_max - row) / (row - 1)
    CR = CI / RI_dict[row]
    print('CR='+str(CR))
    if CR < 0.1:
        print(round(CR, 3))
        print('满足一致性')
        print(np.max(w))
        print(sorted(w,reverse=True))
        print(max_max)
        print('特征向量:%s' % w)
        return w
    else:
        print(round(CR, 3))
        print('不满足一致性，请进行修改')



def language_f(x_array): #语言x
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        if x < 0 :
            result_array[i] = 0
        elif 10 * x < np.max(x_array):
            result_array[i] = (10 * x) / np.max(x_array)
        else:
            result_array[i] = 1
    return result_array


def GDP_f(x_array): #语言x
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        if x < 0.5 * np.mean(x_array):
            result_array[i] = 0
        elif x > 4 * np.mean(x_array):
            result_array[i] = 1
        else:
            result_array[i] = (x-0.5*np.mean(x)) / (2.5 * np.mean(x))
    return result_array

def Culture_f(x_array):#文化软实力
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        result_array[i] = x / np.max(x_array)
    return result_array

def Tech_f(x_array): #科技实力 全球竞争力
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        result_array[i] = x / np.max(x_array)
    return result_array

def Construct_f(x_array): #基础设施建设
    result_array = np.zeros(x_array.shape)
    for i,x in enumerate(x_array):
        result_array[i] = x / np.max(x_array)
    return result_array      


def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df


language_data = data_init(r'模糊数学分析\language.csv') #语言
gdp_data = data_init(r'模糊数学分析\2019GDP.csv') #GDP
culture_data = data_init(r'模糊数学分析\Cultural soft power.csv') #文化软实力
construct_data = data_init(r'模糊数学分析\infrastructure.csv') #基础设施
tech_data = data_init(r'模糊数学分析\Global competitiveness.csv') #科技实力
R = [] #隶属矩阵R 横着为5个指标 竖着为13个国家

country_list = []
for i,country in enumerate(np.array(language_data.Country)):
    contry_data = []
    country_list.append(country)
    contry_data.append(float(language_data[language_data.Country == country].Population))
    contry_data.append(float(gdp_data[gdp_data.Country == country].data))
    contry_data.append(float(culture_data[culture_data.Country == country].data))
    contry_data.append(float(construct_data[construct_data.Country == country].data))
    contry_data.append(float(tech_data[tech_data.Country == country].data))
    R.append(contry_data)



R = np.array(R)
R = R.T
R[0] = language_f(R[0])
R[1] = GDP_f(R[1])
R[2] = Culture_f(R[2])
R[3] = Construct_f(R[3])
R[4] = Tech_f(R[4])

R = R.T

#判断矩阵D
D=np.array([
[1,1/5,1/3,3,3],
[5,1,5,5,5],
[3,1/5,1,3,3],
[1/3,1/5,1/3,1,1],
[1/3,1/5,1/3,1,1],
])

#判断矩阵的最大特征值lamda , 即 对应的特征向量
lamda_max , A = np.linalg.eig(D)


#权重向量A:归一化，即得到特征权重向量 
# Note：根据perron-frobenius定理，这里的特征向量一定是全为正的

print("最大特征值：")
print(lamda_max)
print("归一化后的特征向量：")
print(A)

A = get_w(D) #一致性校验,特征向量,CI CR 计算


#得分向量B = A * R A:归一化后的特征向量 R:隶属矩阵
B = np.dot(A,R.T)
print('final result:')
print(B)


for i,country in enumerate(country_list):
    print(country+ ":" + str(B[i]))
