__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
#Merging csv files & Creating a dataframe
August_1_file = 'E:\Tejas\JK\\a.csv'
df1 = pd.read_csv(August_1_file,skiprows=9,sep=',', header=0,
                          names=['scan no', 'date', 'time', 'raw value', 'calibrated value'])
def get_waterlevel( cal_value ):
    return 1.084*cal_value + 2053
def get_surface_area(cal_value):
   return 0
def get_velocity(cal_value):
    return 0
def get_volume(waterlevel, surface_area, velocity):
    return waterlevel*surface_area*velocity
for index, row in df1.iterrows():
    df1['water level'] = get_waterlevel(row['calibrated value'])
    df1['surface area'] = get_surface_area(row['calibrated value'])
    df1['velocity'] = get_velocity(row['calibrated value'])
    df1['volume'] = get_volume(get_waterlevel(row['calibrated value']),get_surface_area(row['calibrated value']),get_velocity(row['calibrated value']))
print df1.head()
    # create date time index
format = '%d/%m/%Y'+'  '+'%H:%M:%S'
c_str = '24:00:00'
for index, row in df1.iterrows():
    x_str = row['time']
    if x_str == c_str:
        # convert string to datetime object
        r_date = pd.to_datetime(row['date'], format='%d/%m/%Y')
        # add 1 day
        c_date = r_date + timedelta(days=1)
        # convert datetime to string
        c_date = c_date.strftime('%d/%m/%Y')
        c_time = '00:00:00'
        # water_level.loc[:, ('date', index)] = c_date
        # water_level.loc[:, ('time', index)] = c_time
    df1['date'][index] = c_date

    df1['time'][index] = c_time

df1['date_time'] = pd.to_datetime(df1['date'] + df1['time'], format=format)
df1.set_index(df1['date_time'], inplace=True)

#Creating a new database based on time : for eg. 6H = 6 hourly data
# http://stackoverflow.com/questions/17001389/pandas-resample-documentation
df = df1.resample('6H', how=np.mean)
#Plotting the resampled data set
fig=plt.figure()
plt.bar(df.index, df['water level'], width=0.35, color='b')
#Rotating the strings in the X axis
fig.autofmt_xdate(rotation=90)
plt.show()


