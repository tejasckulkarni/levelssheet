__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def get_waterlevel( cal_value ):
    #Equation for calibrated water level values
    return 1.084*cal_value + 2053
    #Similarly equations for water level to surface area values
def get_surface_area(cal_value):
   return 0
def get_velocity(cal_value):
    return 0
def get_volume(waterlevel, surface_area, velolcity):
    return waterlevel*surface_area*velolcity
Agstream_file = 'E:\Tejas\Work\ATREE\RNE\Jakkur_WB_Data\Inlet4_HA_Cap\Stage_data\Raw_Data\JAKKUR_002_001.csv'
Agstream_df = pd.read_csv(Agstream_file,skiprows=9,sep=',', header=0,
                          names=['scan no', 'date', 'time', 'raw value', 'calibrated value'])
for index, row in Agstream_df.iterrows():
    Agstream_df['water level'] = get_waterlevel(row['calibrated value'])
    Agstream_df['surface area'] = get_surface_area(row['calibrated value'])
    Agstream_df['velocity'] = get_velocity(row['calibrated value'])
    Agstream_df['volume'] = get_volume(get_waterlevel(row['calibrated value']),get_surface_area(row['calibrated value']),get_velocity(row['calibrated value']))
print Agstream_df
Agstream_df.to_csv(path_or_buf='E:\Tejas\Work\ATREE\RNE\Jakkur_WB_Data\Inlet4_HA_Cap\Stage_data\Synt_Data\JAKKUR_002_001.csv', sep=',')
   #print row['calibrated value'],get_waterlevel(row['calibrated value'])


