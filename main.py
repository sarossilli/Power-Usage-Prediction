import pandas as pd 
import matplotlib.pyplot as plt

plt.style.use("dark_background")
plt.xlabel('Date')
plt.ylabel('kWh Energy Usage')
plt.title('Personal Power Usage')

data = pd.read_csv(open('Power-Usage/data.csv','r'),index_col="Date")['Quantity']
data.index = pd.to_datetime(data.index, format='%m/%d/%Y')
data = data[:'2/15/2020']
data = data.to_frame()
data['Weekly Moving Average'] = data.rolling(7).mean()

data['Weekly Moving Average'] .plot()

print()
