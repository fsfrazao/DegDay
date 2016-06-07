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
        url= "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?
        format=csv&stationID="5050"&Year="2013"&timeframe=2&submit=Download+Data"

    """
    pass
