""" Plot the Effective Growing Degree Canada
 
 This script plots the effective Growing Degree Days on the map of Canada
 From year 2001 to 2005. 
 Effective Growing Degree Days is the average of the sum of accumulated degree days
 over a period of 5years.

 Usage:
 
 Run script to get the Effective growing degree days of the year 2001-2005 from the commandline
 
 $ python map.py 
"""


import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm as cm2


#Ref:http://matplotlib.org/basemap/users/examples.html  

# The effective GDD average for 5years
EGDD = np.array([1310.1, 554.34, 1098.8, 1388.8, 318.82, 618.9,989.86])

# Create map of canada using Lambert Conformal Conic projection
m = Basemap(projection='lcc',
            #With high resolution
            resolution = 'h',
            #And threshold 10000.0
            area_thresh = 10000.0,
            #Centered at
            lat_0=30.83158,lon_0=-50.,
            lat_1=-4.,
            #longitude of lower left hand corner
            llcrnrlon=-147.9927,
            #latitude of lower left hand corner
            llcrnrlat=45.49,
            #Longitude of upper right hand corner
            urcrnrlon=-36.4459,
            #Latitude of upper left hand corner
            urcrnrlat=72.8125 )

location_data = {'latitude':[43.670495, 53.5444 , 49.406457, 45.500137, 52.139572, 47.570861,44.6488], 
                'longitude':[-79.400041,-113.4909 ,-123.151382,-73.563254 ,-106.646736, -52.707866,-63.5752]}
df = pd.DataFrame(location_data,columns=['latitude', 'longitude'])

labels = ['Toronto','Edmonton','Vancouver', 'Montreal','Saskatoon','St. John\'s',Halifax]

#Define our latitude and longitude points
x,y=m(df['longitude'].values, df['latitude'].values)
for label, xpt, ypt,x_offset, y_offset in zip(labels, x, y,x_offsets,y_offsets):
    plt.text(xpt + x_offset, ypt + y_offset, label,fontweight='bold',zorder=4)


# Draw coastlines 
m.drawcoastlines()

# Draw country borders on the map
m.drawcountries() 

#Draw province borders on the map
m.drawstates()

#Draw map boundries
m.drawmapboundary(fill_color='#99ffff')

#Fill the land with white
m.fillcontinents(color='white',lake_color='#99ffff', zorder=1)

#Draw parallels
parallels = np.arange(0.,90,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

#Draw meridians
meridians = np.arange(180.,360.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

#Plot
m.scatter(x, y, c=EGDD, alpha =0.3, s =2500, cmap=cm2.get_cmap('jet'), zorder=2)
m.scatter(x, y, c=EGDD, alpha=0.3, s=500, cmap=cm2.get_cmap('jet'), zorder=3)
plt.show()


