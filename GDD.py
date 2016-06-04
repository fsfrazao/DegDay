import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Calculate Growing Degree Days.')
parser.add_argument('file', metavar='file', type=str,
                    help='the file for containing daily min and max \
                    temperatures')

args = parser.parse_args()
output_name=args.file.split('.csv')[0]+'_GDD.csv'

def calculate_GDD(min_t, max_t, base_t):
    """ Calculates Growing Degree Days (GDD).

    Args:
        min_t (float): The minimum temperature.
        max_t (float): The maximum temperature.
        base_t (float): The base temperature.

    Returns:
        float: The number of growing degree days.

        This value is always >=0.

    """

    GDD = (min_t + max_t) / 2 - base_t
    GDD=round(GDD, 2)
    return max(GDD,0)


#Read the file passesd as argument into a pandas dataframe
df = pd.read_csv(args.file,sep=',')


gdds=df.apply(lambda row: calculate_GDD(min_t=row['min_t'],\
                max_t=row['max_t'],base_t=10) ,axis=1)

df=pd.concat([df,gdds],axis=1)
df.rename(columns={0:'gdd'},inplace=True)

df.to_csv(output_name,sep=',')
