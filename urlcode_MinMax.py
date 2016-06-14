"""
 This program automates the MinMax Temperature download process by
      assembling the url, cleans the data and
      produce the data meant for MinMax Temperature plotting
    Commandline Args:
        input_MinMax.txt : The editable text file indicating stationid and year
        we could get more stationid and year data by simply adding more to
        stationid to line 0 and years to line 1 of this file
        folder: The folder that saves the data of the years and stationid
        specified by the input_MinMax.txt
    Example Usage: python urlcode_MinMax.py input_GDD.txt folder
 """

import pandas as pd
import os
import sys

def url_assembler(stationid,year):
    """Assembles the url
   
    Retrieves the url pertaining to the given arguments from 
    the environment canada's website 

    Args:
        stationid:A string variable that changes depending on the location 
        year: A string variable that changes ranging from 1894 to 2016
        
    Returns:
        A complete url string that changes depending on the year and stationId args passed.
        For example: if stationid='5050'and year= 2013
        url= "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="5050"&Year="2013"&timeframe=2&submit=Download+Data"

    """

    url="http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="
    url = url+stationid + "&Year="+year+ "&timeframe=2&submit=Download+Data"
    return url

input_file = sys.argv[1]
output_folder = sys.argv[2]
os.popen("mkdir "+ str(output_folder)) #Create a directory for the output

def data_cleaner(url,year,stationid):
    
    """Reads files directly from the url and cleans the data 
   
    Uses python pandas module to read directly from the url,clean the data
    and,index the position and rename the columns.Output to a csvfile. 
    Open the file and remove newline charsplit the string.
    Then loop over the lines to write manipulated output to file
    

    Args:
        url:  The string variable returned by the first function 
        year: A string variable that changes ranging from 1894 to 2016
        stationid : A string variable that changes depending on the user's preference
        
    Returns:
        A completely automated downloaded cleaned csv file
        with just the renamed needed columns of the given stationids and years
        
    """
    output_name=str(output_folder) + '/' + stationid + "_"+ year+".csv"
    data= pd.read_csv(url,sep=',',skiprows=25)#Skip the first 25rows of the url csv file
    #columns= [1,2,3,5,7] # Index by position on the csv 
    columns= [0,5,7]
    clean_data=data[columns]
    clean_data.is_copy = False
    col_names=clean_data.columns
    clean_data.rename(columns={col_names[0]:'date',\
    col_names[1]:'max_temp' ,col_names[2]:'min_temp'},inplace=True)
    clean_data.to_csv(output_name,sep=',',index=False)

with open(input_file,'r')as input_file:
    lines=input_file.readlines()
    lines=[line.rstrip('\n') for line in lines] 
    lines=[tuple(line.split(',')) for line in lines] 

for line in lines:
    stationid=line[0]
    year = line[1]
    url= url_assembler(stationid,year)
    data_cleaner(url,year,stationid)
