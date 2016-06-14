import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as np
import pandas as pd
from datetime import datetime
import sys
from glob import glob
import argparse
import os
import re

def bytespdate2num(fmt, encoding='utf-8'):
    """Converting data stamps for Matplotlib
    
        Args:
            Function bytespdate2num() takes the data, decodes the data based on the encoding, then it returns that.
"""    
    
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter



def read_weather(file_name):
    """Read MinMax csv file

        Args:
            read_weather(file_name): a path to the csv file containing the MinMax data.
"""        
    
    dtypes = np.dtype({ 'names' : ('date','max temp', 'min temp'),
                        'formats' : ['S9', np.float,np.float] })

    dates,max_temp,min_temp = np.loadtxt(file_name, delimiter=',', skiprows=1,
            usecols=(0,1,2),dtype=dtypes,unpack=True,converters={0:dt.bytespdate2num('%Y-%m-%d')})    
    return dates,max_temp,min_temp

def plot_MinMax(csv_file):
    """Plot the Min and Max Temperature curves.
        
        Args:
            os.path.join('/home/darren/Downloads/DegDay/output', csv_file[:-3]+"png") makes three png files save into output directory
            plt.savefig(filename) plot the three png files
    """
    dates,max_temp,min_temp = read_weather(csv_file)
    maxy,=plt.plot_date(dates,max_temp,'r-',label="Max")
    mint,=plt.plot_date(dates,min_temp,'b-',label="Min")
    plt.legend(handles=[maxy,mint])
    plt.title("Min and Max Temperature")
    plt.ylabel("temp")
    plt.xlabel("date")
    #save plot to output directory, this is just my local directory which can be changed.
    filename = os.path.join("../output", csv_file[:-3]+"png")
    plot_min_max = plt.savefig(filename)

path=os.chdir('Task4_input')
csv_folder_file = glob('*.csv')


for i in csv_folder_file:
        
	print(i)
	minmax = plot_MinMax(i)	



