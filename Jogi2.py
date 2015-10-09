_author__ = 'Tejas'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

rootdir= 'C:\\Documents\ and\ Settings\\Guest\\My\ Documents\\Code\\'
#use '\\' in a normal string if you mean to make it be a '\'
#use '\ ' in a normal string if you mean to make it be a ' '


def doWhatYouWant(line):
    print line
    return line
    #let the function return, not only print, to get the value for use as below


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        f=open(rootdir+file,'r') #use the absolute URL of the file
        lines = f.readlines()
        f.close()
        f=open(file,'w') #universal mode can only be used with 'r' mode
        for line in lines:
            newline=doWhatYouWant(line)
            f.write(newline)
        f.close()
