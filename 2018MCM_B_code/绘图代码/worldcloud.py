from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import webbrowser
import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import numpy as np

#data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\2015-2020语言发展情况数据\contry'
data_path=r'C:\Users\Owen\Documents\2018MCM_B_code\2020-2070年全球主要语言情况预测结果'

def get_data(csv_data,years): #传入csv数据 和 language对应的位置信息 返回对应年份的相应数据
    data = csv_data[csv_data.years == years]
    return data.total_users
words = []
max = 0
object_year = 2069
file_list = os.listdir(data_path)
for i,csv_file_name in enumerate(file_list):
    label = csv_file_name.split('_') 
    f = open(os.path.join(data_path,csv_file_name ))
    df = pd.read_csv(f)
    data_one = []
    language = csv_file_name.split('_')[0]
    data_one.append(language)
    data_one.append(float(get_data(df,object_year)))

    if max < float(get_data(df,object_year)):
        max = float(get_data(df,object_year))

    words.append(tuple(data_one))

# words = [
#     ("Sam S Club", 10000),
#     ("Macys", 6181),
#     ("Amy Schumer", 4386),
#     ("Jurassic World", 4055),
#     ("Charter Communications", 2467),
#     ("Chick Fil A", 2244),
#     ("Planet Fitness", 1868),
#     ("Pitch Perfect", 1484),
#     ("Express", 1112),
#     ("Home", 865),
#     ("Johnny Depp", 847),
#     ("Lena Dunham", 582),
#     ("Lewis Hamilton", 555),
#     ("KXAN", 550),
#     ("Mary Ellen Mark", 462),
#     ("Farrah Abraham", 366),
#     ("Rita Ora", 360),
#     ("Serena Williams", 282),
#     ("NCAA baseball tournament", 273),
#     ("Point Break", 265),
# ]
c = (
    WordCloud()
    .add("1111", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="Number of language users wordcloud in 2070"))
    .render(r"C:\Users\Owen\Documents\2018MCM_B_code\map\wordcloud_language.html")
)
