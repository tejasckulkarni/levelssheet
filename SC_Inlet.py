__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def get_waterlevel( cal_value ):
    return 1.084*cal_value + 2053
def get_surface_area(cal_value):
   return 0
def get_velocity(cal_value):
    return 0
def get_volume(waterlevel, surface_area, velolcity):
    return waterlevel*surface_area*velolcity
path ='E:\Tejas\Work\ATREE\RNE\Jakkur_WB_Data\Inlet3_SC_Cap\Stage_data\Raw_Data'
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for 'E:\Tejas\Work\ATREE\RNE\Jakkur_WB_Data\Inlet3_SC_Cap\Stage_data\Raw_Data\' in allFiles':
    df = pd.read_csv('E:\Tejas\Work\ATREE\RNE\Jakkur_WB_Data\Inlet3_SC_Cap\Stage_data\Raw_Data',skiprows=9, header=0,
                     names=['scan no.','date', 'raw value','calibrated value'])
    list_.append(df)
frame = pd.concat(list_)
for index, row in frame.iterrows():
    frame['water level'] = get_waterlevel(row['calibrated value'])
    frame['surface area'] = get_surface_area(row['calibrated value'])
    frame['velocity'] = get_velocity(row['calibrated value'])
    frame['volume'] = get_volume(get_waterlevel(row['calibrated value']),get_surface_area(row['calibrated value']),get_velocity(row['calibrated value']))
print frame

Agstream_df.to_csv(path_or_buf='E:\Tejas\Work\ATREE\RNE\Jakkur_WB_Data\Inlet4_HA_Cap\Stage_data\Synt_Data\JAKKUR_002_001.csv', sep=',')
   #print row['calibrated value'],get_waterlevel(row['calibrated value'])


