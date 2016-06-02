import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Calculate Growing Degree Days.')
parser.add_argument('file', metavar='file', type=str,
                    help='the file for containing daily min and max temperatures')

args = parser.parse_args()
print(args.file)


def load_data(file):
    """ Reads a csv file.

    Args:
        file (string): path to csv file containing min and max temperatures.


    Returns:
        pandas dataframe: the csv file as a dataframe

    """

    




def calculate_GDD(min_t,max_t,base_t):
    """ Calculates Growing Degree Days (GDD).

    Args:
        min_t (float): The minimum temperature.
        max_t (float): The maximum temperature.
        base_t (float): The base temperature.

    Returns:
        float: The number of growing degree days.

        This value is always >=0.

    """

    GDD=(min_t+max_t)/2-base_t

    return round(GDD,2)
