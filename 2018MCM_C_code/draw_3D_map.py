import pyecharts.options as opts
from pyecharts.charts import Bar3D

AZ:38
CA:76
NM:153
TX:42


data_all = [
('AZ',38),
('CA',76),
('NM',153),
('TX',42),
]

contry=[]
data = []
for i,c in enumerate(data_all):
    contry.append(data_all[i][0]) 
    data.append([i,0,data_all[i][1]])

y_label = ["Score"]

#data = [[d[1], d[0], d[2]] for d in data]


(
    Bar3D(init_opts=opts.InitOpts(width="800px", height="800px"))
    .add(
        series_name=opts.Axis3DOpts(type_="category",data=contry),
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=contry,splitnum=0,interval=0),
        yaxis3d_opts=opts.Axis3DOpts(type_="category",name_gap=0),
        zaxis3d_opts=opts.Axis3DOpts(type_="value",data=y_label),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=100,
            range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",

            ],
        )
    )
    .render("bar3d_punch_card.html")
)
