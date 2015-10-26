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





