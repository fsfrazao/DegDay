from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
#Ref:http://matplotlib.org/basemap/users/examples.html  

#Variable names
#llcrnrlon      longitude of lower left hand corner of the selected map domain.
#llcrnrlat      latitude of lower left hand corner of the selected map domain.
#urcrnrlon      longitude of upper right hand corner of the selected map domain.
#urcrnrlat      latitude of upper right hand corner of the selected map domain.

# set up map projection with the variables
# use high resolution coastlines.
m = Basemap(projection='lcc',
            resolution = 'h', 
            lat_1=-4., lat_0=30.83158,
            area_thresh = 10000.0,
            llcrnrlon=-147.9927, 
            llcrnrlat=45.49, 
            urcrnrlon=-36.4459,
            urcrnrlat=72.8125,
            lon_0=-50.)

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
