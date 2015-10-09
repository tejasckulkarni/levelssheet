__author__ = 'kiruba'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import checkdam.evaplib as evap
import checkdam.meteolib as met


noyyal_evap_file = "E:\Tejas\Work\ATREE\RNE\Python\kiruba\vadakalur_evapo.csv"
noyyal_evap_df = pd.read_csv(noyyal_evap_file)
print noyyal_evap_df.head()

noyyal_evap_df['Date'] = pd.to_datetime(noyyal_evap_df['Date'], format="%m/%d/%Y")
noyyal_evap_df.set_index(noyyal_evap_df['Date'], inplace=True)

noyyal_evap_df.sort_index(inplace=True)
noyyal_evap_df['index'] = noyyal_evap_df.index
noyyal_evap_df.drop_duplicates(subset='index', take_last=True, inplace=True)
del noyyal_evap_df['index']
noyyal_evap_df.sort_index(inplace=True)

z = 411
# create new column
noyyal_evap_df['Air_pressure(Pa)'] = noyyal_evap_df['Atmospheric Pressure (hpa)'] * 100.0

lat = 11.0183
lon = 76.9725

noyyal_evap_df['Rext (J/m2/day)'] = 0.000
noyyal_evap_df['sunshine_hours'] = 0.0
for i in noyyal_evap_df.index:
    doy =int(i.strftime('%j'))
    sunshine_hours, rext = met.sun_NR(doy=doy, lat=lat)
    print rext
    noyyal_evap_df.loc[i,'Rext (J/m2/day)'] = rext
    noyyal_evap_df.loc[i,'sunshine_hours'] = sunshine_hours

print noyyal_evap_df.head()

noyyal_evap_df['wind_speed_m_s'] = noyyal_evap_df['Wind Speed(Kmph)'] * 0.277778
noyyal_evap_df['solar_radiation_j_sqm'] = noyyal_evap_df['Solar Radiation']*(41868)
#noyyal_evap_df['average_temp_c'] = 0.5 * (noyyal_evap_df['Max_temp_C'] + noyyal_evap_df['Min_temp_c'])

airtemp = noyyal_evap_df['temp']
hum = noyyal_evap_df['Relative Humidity(%)']
airpress = noyyal_evap_df['Air_pressure(Pa)']
rs = noyyal_evap_df['solar_radiation_j_sqm']
rext = noyyal_evap_df['Rext (J/m2/day)']
sunshine = noyyal_evap_df['sunshine_hours']
wind_speed = noyyal_evap_df['wind_speed_m_s']

noyyal_evap_df['evaporation_mm_day'] = evap.E0(airtemp=airtemp,rh=hum, airpress=airpress, Rs=rs, Rext=rext, u=wind_speed, Z=z )
noyyal_evap_df.to_csv('E:\Tejas\Work\ATREE\RNE\Python\kiruba\noyal_evapa.csv')
print noyyal_evap_df.head()

