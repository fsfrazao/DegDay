# This code cleans the csv file" but only after it is being saved on the system"
# Well I tried using pandas to work with the earlier code but looks like I am not getting it or i probably need more time
# Still working on it though
# Remember you have to download the csv file and save it in same directory or import sys to get this to work

import csv
csv_file_name = 'weather_data_2015.csv'
lines_to_skip = 25

with open(csv_file_name, 'r') as csvfile:
    for i in range(lines_to_skip):
        # throw away the legend inside the csv file
        csvfile.readline()
   
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Date/Time'], row['Min Temp (\xb0C)'])# Print only the needed rows
