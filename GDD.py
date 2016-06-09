""" GDD
This program reads .csv file containing daily min and max temperatures and
calculates the Growing Degree Days for each row in the input file.

It expects one the input directory to passed as the first argument and the output directory to be passed as the second.
It doe not accept a file name as input argument. If only one file is to be processed, it should still be in a directory (with no other file).
GDD.py will try to use all files in the input directory.

Example:

Calculates GDD for all files in the ./my/input/directory/ saves the output files ./my/output/directory directory.

$ python GDD.py ./my/input/directory/ ./my/output/directory
"""


import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(description='Calculate Growing Degree Days.')
parser.add_argument('path', metavar='path', type=str,
                    help='path to the folder containing daily min and max \
                    temperature files')

parser.add_argument('output_dir', metavar='output_dir', type=str,
                    help='path to directory in which outputs will be saved')





args = parser.parse_args()


def calculate_GDD(min_t, max_t, base_t, max_threshold):
    """ Calculates Growing Degree Days (GDD).

    Args:
        min_t (float): The minimum temperature.
        max_t (float): The maximum temperature.
        max_threshold (float): Maximum values for max_t
        base_t (float): The base temperature.


    Returns:
        float: The number of growing degree days.

        This value is always >=0.

    """
    if min_t < base_t: min_t = base_t
    if max_t > max_threshold: max_t = max_threshold
    GDD = (min_t + max_t) / 2 - base_t
    GDD=round(GDD, 2)
    return max(GDD,0)



def read_file(file_path):
    """ Read a .csv file containing min and max temperatures.

    Args:
        file_path (string):The path to the file.

    Returns:
        pandas series: Pandas series object containing the contents of the file.

    """
    file_name=os.path.split(file_path)[1]
    df = pd.read_csv(file_path,sep=',')
    return df

def apply_GDD(data, base_t=10):
    """ Applies the calculate_GDD function to a series containing min and max temperatures.

    Args:
        data (pandas series):Series object containing temperature data.
        base_t (float): The base temperature

    Returns:
        pandas series: Pandas series object containing the contents of the
        data plus a new column with the calculated GDD.
    """


    gdds=data.apply(lambda row: calculate_GDD(min_t=row['min_temp'],\
                    max_t=row['max_temp'],base_t=base_t,max_threshold=30) ,axis=1)

    data=pd.concat([data,gdds],axis=1)
    data.rename(columns={0:'gdd'},inplace=True)

    return data

if __name__=="__main__":

    input_files=os.listdir(args.path)
    for input_file in input_files:
        output_name=args.output_dir+'/'+input_file.split('.csv')[0]+'_GDD.csv'
        data=read_file(file_path=args.path+'/'+input_file)
        output=apply_GDD(data)
        output.to_csv(output_name,sep=',')
