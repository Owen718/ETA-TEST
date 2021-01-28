from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
import pandas as pd
import numpy as np
def AZ():
    return opts.LabelOpts(formatter=JsCode(fn1), position="center")
def CA():
    return opts.LabelOpts(formatter=JsCode(fn2), position="center")
def NM():
    return opts.LabelOpts(formatter=JsCode(fn3), position="center")
def TX():
    return opts.LabelOpts(formatter=JsCode(fn4), position="center")

def data_init(csv_file): #读取一个csv并返回
    f = open(csv_file)
    df = pd.read_csv(f)
    return df

fn1 = """
    function(params) {
        return '\\n AZ';
    }
    """


fn2 = """
    function(params) {
        return '\\n CA';
    }
    """

fn3 = """
    function(params) {
        return '\\n NM';
    }
    """

fn4 = """
    function(params) {
        return '\\n TX';
    }
    """

AZ_1960=[]
AZ_2009=[]
CA_1960=[]
CA_2009=[]
NM_1960=[]
NM_2009=[]
TX_1960=[]
TX_2009=[]


AZ_d = data_init(r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\扇饼图数据\AZ_9个指标60年09年数据.csv')
CA_d = data_init(r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\扇饼图数据\CA_9个指标60年09年数据.csv')
NM_d = data_init(r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\扇饼图数据\NM_9个指标60年09年数据.csv')
TX_d = data_init(r'C:\Users\Owen\Documents\2018MCM_C_code\数据清洗\扇饼图数据\TX_9个指标60年09数据.csv')

for i,MSN in enumerate(AZ_d.MSN):
    AZ_1960.append([MSN,int((AZ_d.y1[i]/np.sum(AZ_d.y1))*100)])
    AZ_2009.append([MSN,int((AZ_d.y2[i]/np.sum(AZ_d.y2))*100)])
for i,MSN in enumerate(CA_d.MSN):
    CA_1960.append([MSN,int((CA_d.y1[i]/np.sum(CA_d.y1))*100)])
    CA_2009.append([MSN,int((CA_d.y2[i]/np.sum(CA_d.y2))*100)])
for i,MSN in enumerate(NM_d.MSN):
    NM_1960.append([MSN,int((NM_d.y1[i]/np.sum(NM_d.y1))*100)])
    NM_2009.append([MSN,int((NM_d.y2[i]/np.sum(NM_d.y2))*100)])
for i,MSN in enumerate(AZ_d.MSN):
    TX_1960.append([MSN,int((TX_d.y1[i]/np.sum(TX_d.y1))*100)])
    TX_2009.append([MSN,int((TX_d.y2[i]/np.sum(TX_d.y2))*100)])




print(AZ_1960)

c = (
    Pie()
    .add(
        "",
        AZ_1960,
        center=["15%", "15%"],
        radius=[40, 50],
        label_opts=AZ(),
    )
    .add(
        "",
        AZ_2009,
        center=["45%", "15%"],
        radius=[40, 50],
        label_opts=AZ(),
    )
    .add(
        "",
        CA_1960,
        center=["15%", "37%"],
        radius=[40, 50],
        label_opts=CA(),
    )
    .add(
        "",
        CA_2009,
        center=["45%", "37%"],
        radius=[40, 50],
        label_opts=CA(),
    )
    .add(
        "",
        NM_1960,
        center=["15%", "59%"],
        radius=[40,50],
        label_opts=NM(),
    )
    .add(
        "",
        NM_2009,
        center=["45%", "59%"],
        radius=[40,50],
        label_opts=NM(),
    )
    .add(
        "",
        TX_1960,
        center=["15%", "81%"],
        radius=[40,50],
        label_opts=TX(),
    )
    .add(
        "",
        TX_2009,
        center=["45%", "81%"],
        radius=[40,50],
        label_opts=TX(),
    )


    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_top="20%", pos_left="60%", orient="vertical"
        ),
    )
    .render("数据图\扇饼图\mutiple_pie.html")
)


