
# coding: utf-8

# In[ ]:

# Provided the input directory containing the .gdd files for a given city over a period of years, the dataframe 'data' 
#coprises the merged data.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import statsmodels.formula.api as smf
from scipy import stats
from datetime import datetime

path =r'./GDD/inputfiles' # use your path
allFiles = glob.glob(path + "/*.csv")
data = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=0)
    list_.append(df)
data = pd.concat(list_)
#data.head()

#The cummulative gdd is plotted over the years
ax= data.groupby(by=['year'])['gdd'].sum().plot(title = 'Cummulative GDD in St. Johns for 5 years',color = 'r', marker = 'o', ls = '')
ax.set(ylabel='Cummulative GDD')

# regression analysis is carried out over gdd and time
lm = smf.ols(formula='data.gdd ~ data.gdd.index', data=data).fit()

# print the coefficients
lm.params
#print the summary
lm.summary()

