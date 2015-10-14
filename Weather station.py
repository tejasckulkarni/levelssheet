__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
weather_file ='E:\Tejas\JK\\WS_22.csv'
df = pd.read_csv(weather_file,sep=',', header=1,
                          names=['id', 'tsUnix', 'P', 'RH','Rain','T','__rssi'])
df['date'] = pd.to_datetime(df['date'],unit='ms')
print df.hear()
for index, row in df.iterrows():
    unix_timestamp = float(str(row['tsUnix'])[0:-4])
    df['Date_Time']= datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y/%m/%d %H:%M:%S')



























