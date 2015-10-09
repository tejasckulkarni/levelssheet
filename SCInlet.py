__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SC_level_file = 'E:\Tejas\PYTHON\JAK_SC_06_10.csv'
SC_level_df = pd.read_csv(SC_level_file,skiprows=9,sep=','', header =0')
format = "%d%m%y" "%H%M%S"
\

SC_level_df["Date_time"]= pd.to_datetime(SC_level_df["Date_time"]),format=format)
SC_level_df.set_index(SC_level_df['Date_Time'],inplace=True)
SClevel6h_df=SC_level_df.resample('6H', how=np.mean)
fig = plt.figure()
plt.bar(SClevel6h_df.index,SClevel6h_df['Water Level_mm'width=0.35,color='b'])
fig.autofmt_xdate(rotation=90)
plt.show()


