""" plot_cummulative_GDD
This program reads .csv files containing daily Growing Degree Days
and produces a cummulative GDD plot with one curve for each file in the input dicrectory



Example:

Make a plot using all the files in the ./my/GDD/input/files directory and save the resulting plot as GDD_Basic_2.png in the ./my/cummulative/plots directory

$ python plot_cummulative_GDD.py ./my/GDD/input/files ./my/cummulative/plots/GDD_Basic_2.png

"""

import argparse
import matplotlib.pyplot as plt
import pandas as pd
import os

parser = argparse.ArgumentParser(description="Plot the cummulative growing degree days for several years in a location")
parser.add_argument("input_folder", help="Path to folder with GDD files to be used in the plot")
parser.add_argument("output_file", help="Path to file in which figuere will be saved")

args = parser.parse_args()

def  cum_gdd_from_file(file_name):
    """Read GDD data from file and return a list with
        the cummulative equivalent.

        Args:
            file (string): a path to the csv file containing the GDD data.

        Returns:
            pandas series (float): a pd series object with the cummulative GDDs

    """
    data=pd.read_csv(file_name,sep=',')
    gdds=data['gdd']
    return gdds.cumsum()

def plot_cum_curves(curves, output_file):
    """Plot the cummulative GDD curves.

        Args:
            curves: a dictionary in which keys are years and\
                    values are lists with a sequence of GDDs

            output_file (string): file path/name in wich the figure will be saved.

    """

    fig=plt.figure()
    ax1=plt.subplot2grid((1,1),(0,0))
    for year in curves.keys():
        ax1.plot(curves[year], label=year)
    plt.title("Cummulative Growing Degree Days")
    plt.xlabel("day")
    plt.ylabel("GDD")
    plt.legend(loc="upper left")

    plt.savefig(output_file)
    plt.close(fig)


GDD_files=os.listdir(args.input_folder)
curves={}
for GDD_file in GDD_files:
    year=GDD_file.split('_')[1]
    curves[year]=cum_gdd_from_file(args.input_folder+'/'+GDD_file)

plot_cum_curves(curves,args.output_file)
