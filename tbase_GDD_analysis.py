import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf



def max_cum_GDD(GDD_file):
    """Read GDD data from file, calculate cummulative GDDs and return the maximum value.

        Args:
            GDD_file (string): a path to the csv file containing the GDD data.

        Returns:
            float: the maximum cummulative GDD

    """
    data=pd.read_csv(GDD_file,sep=',')
    gdds=data['gdd']
    cum_gdd=gdds.cumsum()

    return max(cum_gdds)
