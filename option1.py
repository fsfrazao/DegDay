import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from pandas import Series, DataFrame
import pandas as pd
import csv
import sys
from pylab import *
import io
import os
from glob import glob

fig,ax1=plt.subplots()

def read_weather(file_name):
    
    data=pd.read_csv(file_name, usecols=(1,2,3,4),encoding='ISO-8859-1',delimiter =',') 
    
    data = data.dropna(how='any')
    date = data['date']
    max_temp = data['max_temp']
    min_temp = data['min_temp']
    gdd = data['gdd']
    return data, max_temp, min_temp, gdd


def plot_gdd(filename1, filename2, filename3):
    """
    This  function is to plotting gdd, the function has at most three data file to plot gdd graph.
    """
        
    data_to_plot2 = [filename1,filename2,filename3]
    data_to_plot = [x for x in data_to_plot2 if x is not None]
    data, max_temp, min_temp, gdd = read_weather(filename1)
    index = np.arange(0, 365) 
    
    
    ax1.plot(index,gdd,'bs',label=filename1[5:-8]+" year")
    for i in data_to_plot:
        c=len(data_to_plot)
        data2, max_temp2, min_temp2, gdd2 = read_weather(i)
        new_gdd2=gdd2[0:366]
        y = new_gdd2/c
        grd = plt.grid(True)
        ax1.set_xlabel('Month',fontsize=12)
        plt.xlabel("Month", fontsize=12)
        ax1.set_ylabel('Daily Accumulated based on Celsius',fontsize=15, color='b')
        ax1.set_title('Daily Growing Degress Days',fontsize=20, color='k')   
    ax1.plot(index,y,label="Average",color='red',linewidth=2.5, linestyle="-")
    ax1.legend(loc=2,shadow=True)
  
    filename = os.path.join("/home/darren/Downloads/output", filename1[:-3]+"png")
    plot_min_max = plt.savefig(filename)

path=os.chdir('/home/darren/Downloads')
csv_folder_file = glob('*.csv')
n=size(csv_folder_file)
if n==1:
    gdd=plot_gdd(csv_folder_file[0],None,None)
elif n==2:
    gdd=plot_gdd(csv_folder_file[0],csv_folder_file[1],None)
else:
    gdd=plot_gdd(csv_folder_file[0],csv_folder_file[1],csv_folder_file[2])
