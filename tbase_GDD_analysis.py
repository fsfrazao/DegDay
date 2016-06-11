import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
import GDD
import os

parser = argparse.ArgumentParser(description="Plot the relationship between max growing degree days and base temperature")
parser.add_argument("input_dir", help="Path to folder with GDD files to be used in the plot")
parser.add_argument("output_figure", help="Path to file in which figure will be saved")

args = parser.parse_args()




def max_cum_GDD(gdds):
    """Read GDD data from file, calculate cummulative GDDs and return the maximum value.

        Args:
            GDD_file (string): a path to the csv file containing the GDD data.

        Returns:
            float: the maximum cummulative GDD.

    """
    cum_gdd=gdds.cumsum()
    return max(cum_gdd)



def base_t_range(data,name,start=0,end=30):
    """Calculate the max cummulative GDD for varying values of base_t.

        The range of base temperatures goes from 'start' to 'end' increasing by 1.

        Args:
            data(pandas series or dataframe): Min and M temperature
                                data from wich GDD is calculated.
            name(string): name to be used in the gdd column of the
                         resulting DataFrame
            start(integer): First value for base_t
            end(integer): Last value for base_t

        Returns:
            pandas DataFrame: 2 columns dataframe. First column
                 ("base_t") is the value used for base temperature.
                 Second column (labeled with the name argument) contains the max cummulative gdd for the corresponding base temperature
    """

    max_gdds={"base_t":[],"gdd":[]}

    for base_t in range(start,end):
        gdd_data=GDD.apply_GDD(data,base_t=base_t)
        max_gdds["base_t"].append(base_t)
        max_gdds["gdd"].append(max_cum_GDD(gdd_data['gdd']))

        df=pd.DataFrame(max_gdds)
        df.rename(columns={"gdd":name},inplace=True)


    return df


data_files=os.listdir(args.input_dir)
name=data_files[0].split('.csv')[0]
data=GDD.read_file(args.input_dir+'/'+data_files[0])
baset_GDD=base_t_range(data=data,name=name)

for data_file in data_files[1:]:
    name=data_file.split('.csv')[0]
    data=GDD.read_file(args.input_dir+'/'+data_file)
    df=base_t_range(data=data,name=name)
    baset_GDD=pd.merge(baset_GDD,df)


baset_GDD=pd.melt(baset_GDD,id_vars='base_t',value_vars=[c for c in baset_GDD.columns[1:]])
fit=np.polyfit(x=baset_GDD["base_t"],y=baset_GDD["value"],deg=2)
model=np.poly1d(fit)

groups=baset_GDD.groupby("variable")


colors = pd.tools.plotting._get_standard_colors(len(groups), color_type='random')


fig,axis=plt.subplots()
axis.set_color_cycle(colors)
for name, group in groups:
    axis.plot(group.base_t,group.value,marker='o',linestyle='',ms=5,label=name)
axis.set_ylim([-100,baset_GDD["value"].max()+.05*baset_GDD["value"].max()])
axis.set_xlim([-1,baset_GDD["base_t"].max()+1])

axis.plot(model(range(30)),ls='-',lw=2,color="black")
a,b,c=fit
plt.xlabel("Base temperature (ºC)")
plt.ylabel("Max Cummulative GDD")
plt.title("GDD={:.2f}.base_t²+{:.2f}.base_t+{:.2f}".format(a,b,c))


axis.legend(numpoints=1,loc='upper right')

#fig=baset_GDD.plot(kind='scatter',x='base_t',y='value')
plt.savefig(args.output_figure)
