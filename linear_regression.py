
# coding: utf-8

# """""This function takes as argument the path to the directory containing all the input files and returns a the plotog the cummulative GDD over a period of time.
# it also takes the summary and stores it in a txt file called learnedmodel.txt""""

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
from datetime import datetime
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import statsmodels.formula.api as smf
import argparse
import os
import time

parser = argparse.ArgumentParser(description="Fit a linear model to the cummulative growing degree days data over several years (explanatory variable)make a plot")
parser.add_argument("input_dir", help="Path to folder with GDD files to be used in the model")
parser.add_argument("output_file", help="Path to file in which figure will be saved")

args = parser.parse_args()

def merge_gdd(input_dir, output_file):
    #path = open(input_dir+"/*.csv", "r")
    allFiles = glob.glob(input_dir + "/*.csv")
    data = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=0)
        list_.append(df)
    data = pd.concat(list_)
    data=data.fillna(0)
    data.date= pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['year'] = data['date'].dt.year
    data['Asum']= data.gdd.cumsum()
    g1= data.groupby(by=['year'])['gdd'].sum()
    df = g1.to_frame()
    df['year'] = df['gdd'].index
    lm = smf.ols(formula='gdd ~ year', data=df).fit()
    lm.params
    lm.summary()
    result=lm.fittedvalues
    with open('learnedmodel.txt','w') as f:
        f.write(lm.summary().as_latex())
    #plt.ion()
    ax=df.plot(kind='scatter', x='year', y='gdd',label='cum gdd')
    plt.plot(df.year,result, c='red', linewidth=2)
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    ax.set(ylabel='Cummulative GDD')
    ax.set(title='Linear Regression')
    tm=str(time.time())

    plt.savefig(output_file)

merge_gdd(input_dir=args.input_dir, output_file=args.output_file)







# In[ ]:
