__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import checkdam.checkdam as cd

from datetime import timedelta

"""
Read Check dam data
"""
block_1 = 'E:\Tejas\JK\\a.csv'
water_level_1 = cd.read_correct_ch_dam_data(block_1, 0.922, -1893)
block_2 = 'E:\Tejas\JK\\b.csv'
water_level_2 = cd.read_correct_ch_dam_data(block_2, 0.922, -1893)
block_3 = 'E:\Tejas\JK\\c.csv'
water_level_3 = cd.read_correct_ch_dam_data(block_2, 0.922, -1893)

for i in range(1, 3, 1):
    eval("water_level_{0}.drop(water_level_{0}.tail(1).index, inplace=True, axis=0)".format(i))
    eval("water_level_{0}.drop(water_level_{0}.head(1).index, inplace=True, axis=0)".format(i))

# for i in range(1, 11, 1):
#     print "water_level_{0}".format(i)
#     print eval("water_level_{0}.head()".format(i))
fig = plt.figure()
for i in range(1, 3, 1):
    x = eval("water_level_{0}.index".format(i))
    y = eval("water_level_{0}['stage(m)']".format(i))
    plt.plot(x, y)

plt.show()
# print water_level_13.head()
raise SystemExit(0)

water_level_30min = pd.concat([water_level_1, water_level_2, water_level_3], axis=0)
water_level_30 = water_level_30min.sort()
rounded = np.array(water_level_30min.index, dtype='datetime64[m]')
water_level_30min = water_level_30min.set_index(rounded)
start_time_30 = min(water_level_30min.index)
end_time_30 = max(water_level_30min.index)
# new_index_30min = pd.date_range(start=start_time_30.strftime('%Y-%m-%d %H:%M'), end=end_time_30.strftime('%Y-%m-%d %H:%M'), freq='30min')
# if type(new_index_30min) is list:
#     print "list"
# else:
#     print "no"
# raise SystemExit(0)
new_index_30 = pd.date_range(start=start_time_30, end=end_time_30, freq='30min')
water_level_30min = water_level_30min.reindex(new_index_30, method=None)
water_level_30min = water_level_30min.interpolate(method='time')
# water_level_30min = water_level_30min.set_index(new_index_30min)
water_level_30min.index.name = 'Date'
print water_level_30min.head()

# raise SystemExit(0)
water_level_10min = pd.concat([water_level_6, water_level_7, water_level_8, water_level_9, water_level_10, water_level_11, water_level_12], axis=0)
water_level_10min = water_level_10min.sort()
rounded = np.array(water_level_10min.index, dtype='datetime64[m]')
water_level_10min = water_level_10min.set_index(rounded)
start_time_10 = min(water_level_10min.index)
end_time_10 = max(water_level_10min.index)
# new_index_10min = pd.date_range(start=start_time_10.strftime('%Y-%m-%d %H:%M'), end=end_time_10.strftime('%Y-%m-%d %H:%M'), freq='10min')
new_index_10 = pd.date_range(start=start_time_10, end=end_time_10, freq='10min')
water_level_10min = water_level_10min.reindex(new_index_10, method=None)
water_level_10min = water_level_10min.interpolate(method='time')
# water_level_10min = water_level_10min.set_index(new_index_10min)
water_level_10min.index.name = 'Date'

water_level = pd.concat([water_level_30min, water_level_10min], axis=0)
water_level = water_level.resample('30min', how=np.mean, label='right', closed='right')
water_level = water_level[:'2015-02-09']
print water_level.tail()
# raise SystemExit(0)
# water_level['stage(m)'] = cd.myround(water_level['stage(m)'], decimals=2)
water_level.to_csv('E:\Tejas\JK\\d.csv')
hour = water_level.index.hour
minute = water_level.index.minute
eleven_30_df = water_level[((hour == 23) & (minute == 30))]
print eleven_30_df.head()
fig = plt.figure()
plt.plot(eleven_30_df.index, eleven_30_df['raw value'], 'ro')
plt.show()
# raise SystemExit(0)
# raise SystemExit(0)






