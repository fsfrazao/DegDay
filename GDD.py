import argparse

parser = argparse.ArgumentParser(description='Calculate Growing Degree Days.')
parser.add_argument('file', metavar='file', type=str,
                    help='the file for containing daily min and max temperatures')

args = parser.parse_args()
print(args.file)


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
