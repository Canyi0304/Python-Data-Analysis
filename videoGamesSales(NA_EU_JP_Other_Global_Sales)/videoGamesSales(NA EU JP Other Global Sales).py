import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#한글폰트
#plt.rcParams['font.family'] ='Malgun Gothic'


data  = pd.read_csv('vgsales.csv')

Market_5 = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']


Market_5_data = pd.pivot_table(data, index = 'Year', values = Market_5 ,aggfunc = np.sum)
plt.figure(figsize=(20,6))
# sns.lineplot(data = Market_5_data, size_order= 10)
sns.lineplot(data = Market_5_data)
plt.title('MarKet Process')

plt.show()

