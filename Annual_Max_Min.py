import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import numpy as np
import pandas as pd
from datetime import datetime

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def read_weather(file_name):

    dtypes = np.dtype({ 'names' : ('date','max temp', 'min temp'),
                        'formats' : ['S9', np.float,np.float] })

    dates,max_temp,min_temp = np.loadtxt(file_name, delimiter=',', skiprows=1,
            usecols=(0,1,2),dtype=dtypes,unpack=True,converters={0:dt.bytespdate2num('%Y-%m-%d')})    
    return dates,max_temp,min_temp

dates,max_temp,min_temp=read_weather('1706_2010.csv')
maxy,=plt.plot_date(dates,max_temp,'r-',label="Max")
mint,=plt.plot_date(dates,min_temp,'b-',label="Min")
plt.legend(handles=[maxy,mint])
plt.title("1706's 2010 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.show()

dates,max_temp,min_temp=read_weather('889_2010.csv')
maxy,=plt.plot_date(dates,max_temp,'r-',label="Max")
mint,=plt.plot_date(dates,min_temp,'b-',label="Min")
plt.legend(handles=[maxy,mint])
plt.title("889's 2010 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.show()

dates,max_temp,min_temp=read_weather('6720_2010.csv')
maxy,=plt.plot_date(dates,max_temp,'r-',label="Max")
mint,=plt.plot_date(dates,min_temp,'b-',label="Min")
plt.legend(handles=[maxy,mint])
plt.title("6720's 2010 temp")
plt.ylabel("temp")
plt.xlabel("date")
plt.show()