
import sys
import pandas as pd
def url_assembler(stationid,year):
  
    """Assembles the url based on the specification on the input file
       Retrieves the url pertaining to the given arguments
    Args:
        stationid:A string variable that changes depending on the input_GDD.txt$
        year: A string variable on the line 1 of input_GDD.txt file
        
    Returns:
        None
    """
    url="http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="
    url = url+stationid + "&Year="+year+ "&timeframe=2&submit=Download+Data"
    return url

first_arg = sys.argv[1] #First commandline arguement
second_arg = sys.argv[2]# Second commandline arguement

def data_cleaner(url,year,stationid):
    
    """Reads files directly from the url and cleans the data 
   
    Uses python pandas module to read directly from the url,clean the data
    and,index the positio and rename the columns. 
    It works with the given lines in the input_Gdd.txt and output to a folder
    

    Args:
        url:  The string variable returned by the first function 
        year: A string variable on line 1 of the input_Gdd.txt file
        stationid : A string variable that changes depending 
        on the entry on input_GDD.txt file

    Commandline Args:
        input_GDD.txt : The editable text file indicating stationid and year
        we could get more stationid and year data by simply adding more to
        stationid to line 0 and years to line 1 of this file
        
        folder: The folder that saves the data of the years and stationid 
        specified by the input_GDD.txt
    
    Returns:
        None
    """
    global second_arg
    output_name=str(second_arg) + '/' + stationid + "_"+ year+".csv"
    data= pd.read_csv(url,sep=',',skiprows=25)#Skip the first 25rows of the url csv file
    columns= [1,2,3,5,7] # Index by position on the csv 
    clean_data=data[columns]
    col_names=clean_data.columns
    clean_data.rename(columns={col_names[0]:'year',col_names[1]:'month',col_names[2]:'day',\
    col_names[3]:'max_temp' ,col_names[4]:'min_temp'},inplace=True)
    clean_data.to_csv(output_name,sep=',',index=False)

with open(first_arg,'r')as input_file:
    lines=input_file.readlines()
    lines=[line.rstrip('\n') for line in lines] 
    lines=[tuple(line.split(',')) for line in lines] 

for line in lines:
    stationid=line[0]
    year = line[1]
    url= url_assembler(stationid,year)
    data_cleaner(url,year,stationid)
