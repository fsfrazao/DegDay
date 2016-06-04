import matplotlib.pyplot as plt
import pandas as pd

def  read_data(file_name):
    """Read GDD data from file and return a list with
        the cummulative equivalent.

        Args:
            file (string): a path to the csv file containing the GDD data.

        Returns:
            list (float): a list with the cummulative GDDs

    """
    data=pd.read_csv(file_name,sep=',')
    gdds=data['gdd']
    return gdds.cumsum()

    
