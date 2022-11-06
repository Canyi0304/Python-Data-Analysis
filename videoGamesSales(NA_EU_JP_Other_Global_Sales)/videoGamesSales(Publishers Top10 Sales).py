import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#한글폰트
#plt.rcParams['font.family'] ='Malgun Gothic'


data  = pd.read_csv('vgsales.csv')

Publisher_Top10 = data['Publisher'].value_counts().head(10).index.tolist()
#print(Publisher_Top10)

Publisher_Top10_data = data[data['Publisher'].isin(Publisher_Top10)]
Publisher_Top10_data_S = pd.pivot_table(data = Publisher_Top10_data, index = 'Year', 
                            columns='Publisher', values = 'Global_Sales', aggfunc=np.sum)
Publisher_Top10_data_S.plot(title = 'Top 10 Publishers Sales', figsize=(15,5))
plt.show()

