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


#Variable names
#llcrnrlon      longitude of lower left hand corner of the selected map domain.
#llcrnrlat      latitude of lower left hand corner of the selected map domain.
#urcrnrlon      longitude of upper right hand corner of the selected map domain.
#urcrnrlat      latitude of upper right hand corner of the selected map domain.


# Create map of canada using Lambert Conformal Conic projection
m = Basemap(projection='lcc',
            #With high resolution
            resolution = 'h', 
            #And threshold 10000.0
            area_thresh = 10000.0,
            #Centered at 
            lat_0=30.83158,lon_0=-50.,
            lat_1=-4., 
            llcrnrlon=-147.9927, 
            llcrnrlat=45.49, 
            urcrnrlon=-36.4459,
            urcrnrlat=72.8125 ) 

# Draw coastlines and country boundaries, edge of map.
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')
m.drawcoastlines()
m.drawcountries() 
m.drawstates()

#Draw parallels
m.drawparallels(np.arange(10,70,20),labels=[1,1,0,0])
#Draw meridians
m.drawmeridians(np.arange(-100,0,20),labels=[0,0,0,1])
plt.show()
