from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
#Ref:http://matplotlib.org/basemap/users/examples.html  

#Variable names
#llcrnrlon      longitude of lower left hand corner of the selected map domain.
#llcrnrlat      latitude of lower left hand corner of the selected map domain.
#urcrnrlon      longitude of upper right hand corner of the selected map domain.
#urcrnrlat      latitude of upper right hand corner of the selected map domain.

#Lambert conformal Conic map
m = Basemap(llcrnrlon=-147.9927, llcrnrlat=45.49, urcrnrlon=-36.4459, urcrnrlat$
              projection='lcc', resolution = 'h', area_thresh = 10000.0,
lat_1=-5., lat_0=31.84256, lon_0=-53.)

# Draw coastlines and country boundaries, edge of map.
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')
m.drawcoastlines()
m.drawcountries() 
m.drawstates()
