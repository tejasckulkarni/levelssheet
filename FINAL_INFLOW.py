__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
#Merging csv files & Creating a dataframe
August_1_file = 'E:\Tejas\JK\\a.csv'
df1 = pd.read_csv(August_1_file,skiprows=9,sep=',', header=0,
                          names=['scan no', 'date', 'time', 'raw value', 'calibrated value'])
August_2_file = 'E:\Tejas\JK\\b.csv'
df2 = pd.read_csv(August_2_file,skiprows=9,sep=',', header=0,
                          names=['scan no', 'date', 'time', 'raw value', 'calibrated value'])
September_file = 'E:\Tejas\JK\\c.csv'
df3 = pd.read_csv(September_file,skiprows=9,sep=',', header=0,
                          names=['scan no', 'date', 'time', 'raw value', 'calibrated value'])
frames = [df1,df2,df3]
df=pd.concat(frames)
#defining functions
def get_waterlevel(cal_value):
    return ((0.922*cal_value)-1893)
def get_surface_area(cal_value):
   return 0
def get_velocity(cal_value):
    return 0
def get_volume(waterlevel, surface_area, velocity):
    return waterlevel*surface_area*velocity
#looping the functions to get desired columns
for index, row in df.iterrows():
    df['water level'] = get_waterlevel(row['calibrated value'])
    df['surface area'] = get_surface_area(row['calibrated value'])
    df['velocity'] = get_velocity(row['calibrated value'])
    df['volume'] = get_volume(get_waterlevel(row['calibrated value']),get_surface_area(row['calibrated value']),get_velocity(row['calibrated value']))
#print df.head()
# create date time index to avoid the 24:00:00 as it cannot be read by pandas
format = '%d/%m/%Y  %H:%M:%S'
c_str = ' 24:00:00'
for index, row in df.iterrows():
    x_str = row['time']
    if x_str == c_str:
        # convert string to datetime object
        r_date = pd.to_datetime(row['date'], format='%d/%m/%Y ')
        # add 1 day
        c_date = r_date + timedelta(days=1)
        # convert datetime to string
        c_date = c_date.strftime('%d/%m/%Y ')
        c_time = ' 00:00:00'
        df['date'][index] = c_date
        df['time'][index] = c_time
#defining date and time index to the dataframe
df['date_time'] = pd.to_datetime(df['date'] + df['time'], format=format)
df.to_csv('E:\Tejas\\JK\Synth_data.csv')
# Resample data to 6H data
#df.set_index(df['date_time'],inplace=True )
#df_6H = df.resample('6H',how=np.sum,label='right',closed='right')
#fig=plt.figure()
#plt.bar(df.index, df['water level'], width=0.35, color='b')
#Rotating the strings in the X axis
#fig.autofmt_xdate(rotation=90)
#plt.show()
