import matplotlib.pyplot as plt
import pandas as pd
import os

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
