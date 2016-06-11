import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

#Ref:http://matplotlib.org/basemap/users/examples.html  

location_data = {'latitude':[43.670495, 53.5444 , 49.406457, 45.500137, 52.139572, 47.570861], 
                'longitude':[-79.400041,-113.4909 ,-123.151382,-73.563254 ,-106.646736, -52.707866]}
df = pd.DataFrame(location_data,columns=['latitude', 'longitude'])

labels = ['Toronto','Edmonton','Vancouver', 'Montreal','Saskatoon','St. John\'s']
x_offsets = [10000, -30000, -25000 , -25000, -30000 , -25000, 10000]
y_offsets = [5000, -25000, -25000 , -25000, 5000, 4000 ,-25000, 10000]
for label, xpt, ypt,x_offset, y_offset in zip(labels, x, y,x_offsets,y_offsets):
    plt.text(xpt + x_offset, ypt + y_offset, label)


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

# Draw coastlines 
m.drawcoastlines()

# Draw country borders on the map
m.drawcountries() 

#Draw province borders on the map
m.drawstates()

#Draw map boundries
m.drawmapboundary(fill_color='#99ffff')

#Fill the land with white
m.fillcontinents(color='white',lake_color='#99ffff')

#Define our latitude and longitude points
x,y=m(df['longitude'].values, df['latitude'].values)

#Draw parallels
parallels = np.arange(0.,90,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)

#Draw meridians
meridians = np.arange(180.,360.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

#Plot them using round markers of size 6
m.plot(x,y,  'bo', markersize=6)

#show the map
plt.show()


