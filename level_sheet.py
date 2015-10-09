__author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#water level file
level_file = 'E:\Tejas\Work\Biome\Hobo_Biome.csv'
#converting csv file to pandas dataframe
level_df = pd.read_csv(level_file, sep='\t', header=0)
#Printing first 5 lines in the csv file. Similarly tail () include no. of line to be seen.
print level_df.head()
format= '%m/%d/%Y %H:%M'
#First we gave the format for the date and time in the CSV. Then we are asking pandas to change the string format to Date_time object.
level_df["Date_Time"]= pd.to_datetime(level_df["Date_Time"], format=format)
#Pandas will convert the Sl.no (existing index) to an index based on Date time.
level_df.set_index(level_df['Date_Time'], inplace=True)
#Creating a new database based on time : for eg. 6H = 6 hourly data
# http://stackoverflow.com/questions/17001389/pandas-resample-documentation
leveldaily_df = level_df.resample('D', how=np.mean)
#Plotting the resampled data set
fig=plt.figure()
plt.bar(leveldaily_df.index, leveldaily_df['Water Level_m'], width=0.35, color='b')
#Rotating the strings in the X axis
fig.autofmt_xdate(rotation=90)
plt.show()





