from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import webbrowser
import matplotlib.pyplot as plt
import csv
import os
import pandas as pd
import numpy as np

def get_data(csv_data,years): #传入csv数据 和 language对应的位置信息 返回对应年份的相应数据
    data = csv_data[csv_data.years == years]
    return data.population

# data_path = r'C:\Users\Owen\Documents\2018MCM_B_code\predict_results'


# data = []
# max = 0
# object_year = 2040
# file_list = os.listdir(data_path)
# for i,csv_file_name in enumerate(file_list):
#     label = csv_file_name.split('_') 
#     f = open(os.path.join(data_path,csv_file_name ))
#     df = pd.read_csv(f)
#     data_one = []
    
#     contry_name = csv_file_name.split('_')[0]
    
#     if contry_name == 'USA':
#         data_one.append('United States')
#     else:
#         data_one.append(contry_name)
#     data_one.append(float(get_data(df,object_year)))

#     if max < float(get_data(df,object_year)):
#         max = float(get_data(df,object_year))

#     data.append(tuple(data_one))

data = [
('China',0.39720680802348207),
('India',0.428204506858802),
('United States',0.9900211345279509),
('Indonesia',0.25435192493187775),
('Pakistan',0.22443288336625428),
('Russia',0.2716981968410572),
('Mexico',0.23960730965952579),
('Japan',0.41512566422813746),
('Germany',0.3788820193003114),
('France',0.36787672949125005),
('United Kingdom',0.36998327311319723),
('Thailand',0.19096693756015007),
('Canada',0.24695474209259038)
]


# data = [
# ('China',52),
# ('Canada', 105),
# ('Brazil', 130),
# ('Russia', 99),
# ('United States', 26),
# ('Africa', 50),
# ('Germany', 131),
# ]

c = (
    Map()
    .add('score',data, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title='Influence Index of nations',title_textstyle_opts=opts.TextStyleOpts(font_size=15)),
        visualmap_opts=opts.VisualMapOpts(max_=1),
    )
    .render(r"C:\Users\Owen\Documents\2018MCM_B_code\map\map_world.html")
)

