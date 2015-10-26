__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import time
weather_file ='E:\Tejas\JK\\data_27.csv'
df = pd.read_csv(weather_file,sep=',', header=1,
                          names=['id', 'tsUnix', 'P', 'RH','Rain','T','__rssi'])
df['timestamp'] = pd.to_datetime(df[('tsUnix')],unit='ms')
print df.head()['timestamp']