import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import argparse
import GDD

parser = argparse.ArgumentParser(description="Plot the relationship between max growing degree days and base temperature")
parser.add_argument("input_file", help="Path to folder with GDD files to be used in the plot")
parser.add_argument("output_figure", help="Path to file in which figure will be saved")

args = parser.parse_args()




def max_cum_GDD(gdds):
    """Read GDD data from ile, calculate cummulative GDDs and return the maximum value.

        Args:
            GDD_file (string): a path to the csv file containing the GDD data.

        Returns:
            float: the maximum cummulative GDD.

    """
    cum_gdd=gdds.cumsum()
    return max(cum_gdd)
