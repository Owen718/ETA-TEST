import pandas as pd
import numpy as np
from fbprophet import  Prophet
import matplotlib.pyplot as plt

data=pd.read_csv('399300.csv',encoding='GB2312')


df = data[[u'time',u'price']]

df.columns = ['ds','y']
df['y'] = df['y'].apply(lambda x:np.log(int(x)))

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=10)
forecast = m.predict(future)

future_predict = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(15)
future_predict['yhat'] = future_predict['yhat'].apply(lambda x:np.exp(x))
future_predict['yhat_lower'] = future_predict['yhat_lower'].apply(lambda x:np.exp(x))
future_predict['yhat_upper'] = future_predict['yhat_upper'].apply(lambda x:np.exp(x))

print(future_predict.ds,future_predict.yhat)

fig1 = m.plot(forecast)  #成分拆分，国内股市的趋势以及季节性因素
plt.show()

fig2 = m.plot_components(forecast) #时间序列的分量
plt.show()
