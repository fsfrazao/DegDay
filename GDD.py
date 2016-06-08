import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(description='Calculate Growing Degree Days.')
parser.add_argument('path', metavar='path', type=str,
                    help='the path for file or folder containing daily min and max \
                    temperatures')

parser.add_argument('output_dir', metavar='output_dir', type=str,
                    help='path to directory in which outputs will be saved')

parser.add_argument('--folder',action='store_true',
                    help='Interprets the given path as a directory and\
                    calculate GDD for all files within.')



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



def process_file(file_path,output_dir ):
    """ Applies the calculate_GDD function to a file.

        An output file will be created in the output_dir.
        The name of this file is the name of the input file
        with '_GDD.csv' in the end.
        Its contents are the five columns in the input file + a 'gdd' column with the calculated results.

    Args:
        file_path (string): Path to the input csv file.
        output_dir (string): Path to the directory in which the
                             resulting file will be stored.

    Returns:
        None
    """

    file_name=os.path.split(file_path)[1]
    output=output_dir+'/'+file_name.split('.csv')[0]+'_GDD.csv'

    df = pd.read_csv(file_path,sep=',')


    gdds=df.apply(lambda row: calculate_GDD(min_t=row['min_temp'],\
                    max_t=row['max_temp'],base_t=10,max_threshold=30) ,axis=1)

    df=pd.concat([df,gdds],axis=1)
    df.rename(columns={0:'gdd'},inplace=True)

    df.to_csv(output,sep=',')

if args.folder:
    input_files=os.listdir(args.path)
    for input_file in input_files:
        process_file(file_path=args.path+'/'+input_file, output_dir=args.output_dir)
    """
    print(args.output_dir)
    """
else:
    process_file(args.path, args.output_dir)
