import pyecharts.options as opts
from pyecharts.charts import Bar3D




data_all = [
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

contry=[]
data = []
for i,c in enumerate(data_all):
    contry.append(data_all[i][0]) 
    data.append([i,0,int(data_all[i][1]*100)])

y_label = ["Score"]

#data = [[d[1], d[0], d[2]] for d in data]


(
    Bar3D(init_opts=opts.InitOpts(width="800px", height="800px"))
    .add(
        series_name=opts.Axis3DOpts(type_="category",data=contry),
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=contry,splitnum=0,interval=0),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=y_label,name_gap=0),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
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
