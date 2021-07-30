import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.image import pil_to_array

m=Basemap(projection='spstere',lon_0=180,boundinglat=-60)

def grid_points(latsize, lonsize, n, idx, lat, long):
    
    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)
    mapV=np.zeros([len(latbin)-1,len(longbin)-1])
    
    if idx.sum()>0:
        x1=lat[idx].values                                 
        y1=long[idx].values
        n1=n[idx]
    
        for i,latk in enumerate(latbin[:-1]):
            for j,lonj in enumerate(longbin[:-1]):
                idx=(x1 >= latk) & (x1 < (latk+latsize)) & (y1 >= lonj) & (y1 < (lonj+lonsize))
                mapV[i,j]=n1[idx].sum()*0.180*5*0.09

        return mapV

def antarc_volume(filename,latsize,lonsize):
    data=xr.open_dataset(filename)
    lat=data.Latitude
    long=data.Longitude
    T=data.Temperature
    compo=data.PSC_Composition 

    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)
    
    idx=(((compo.values==1).sum(axis=1))>0)
    nsts=((compo.values==1).sum(axis=1))
    mapVsts=grid_points(latsize, lonsize, nsts, idx, lat, long) 
    
    idx=((T.values<192).sum(axis=1)>0)
    Tsts=((T.values<192).sum(axis=1))
    mapvTsts=grid_points(latsize, lonsize, Tsts, idx, lat, long)
    
    c=((compo.values==2)|(compo.values==3)|(compo.values==5))                        
    idx=(c.sum(axis=1)>0)
    nnat=(c.sum(axis=1))
    mapVnat=grid_points(latsize, lonsize, nnat, idx, lat, long)
    
    idx=((T.values<195.7).sum(axis=1)>0)
    Tnat=((T.values<195.7).sum(axis=1))
    mapvTnat=grid_points(latsize, lonsize, Tnat, idx, lat, long)
    
    c=((compo.values==4)|(compo.values==6))                        
    idx=(c.sum(axis=1)>0)
    nice=(c.sum(axis=1))
    mapVice=grid_points(latsize, lonsize, nice, idx, lat, long)
    
    idx=((T.values<188.5).sum(axis=1)>0)
    Tice=((T.values<188.5).sum(axis=1))
    mapvTice=grid_points(latsize, lonsize, Tice, idx, lat, long)


    plt.figure(figsize=(7,7))
    x,y = m(*np.meshgrid(longbin,latbin))
    h1=m.pcolormesh(x,y,mapVsts)
    m.drawcoastlines(color='white')
    m.drawparallels(range(-80,-50,2))
    m.drawmeridians(range(-180,180,2))
    plt.colorbar(label='Volume (km3)')
    plt.title(u'Volume de PSC STS')
    plt.show()

    plt.figure(figsize=(7,7))
    x,y = m(*np.meshgrid(longbin,latbin))
    h2=m.pcolormesh(x,y,mapvTsts)
    m.drawcoastlines(color='white')
    m.drawparallels(range(-80,-50,2))
    m.drawmeridians(range(-180,180,2))
    plt.colorbar(label='Volume (km3)')
    plt.title(u'Volume de temperature T<Tsts')
    plt.show()
    
    plt.figure(figsize=(7,7))
    x,y = m(*np.meshgrid(longbin,latbin))
    h3=m.pcolormesh(x,y,mapVnat)
    m.drawcoastlines(color='white')
    m.drawparallels(range(-80,-50,2))
    m.drawmeridians(range(-180,180,2))
    plt.colorbar(label='Volume (km3)')
    plt.title(u'Volume de PSC NAT')
    plt.show()

    plt.figure(figsize=(7,7))
    x,y = m(*np.meshgrid(longbin,latbin))
    h4=m.pcolormesh(x,y,mapvTnat)
    m.drawcoastlines(color='white')
    m.drawparallels(range(-80,-50,2))
    m.drawmeridians(range(-180,180,2))
    plt.colorbar(label='Volume (km3)')
    plt.title(u'Volume de temperature T<Tnat')
    plt.show()
    
    plt.figure(figsize=(7,7))
    x,y = m(*np.meshgrid(longbin,latbin))
    h5=m.pcolormesh(x,y,mapVice)
    m.drawcoastlines(color='white')
    m.drawparallels(range(-80,-50,2))
    m.drawmeridians(range(-180,180,2))
    plt.colorbar(label='Volume (km3)')
    plt.title(u'Volume de PSC Ice')
    plt.show()

    plt.figure(figsize=(7,7))
    x,y = m(*np.meshgrid(longbin,latbin))
    h6=m.pcolormesh(x,y,mapvTice)
    m.drawcoastlines(color='white')
    m.drawparallels(range(-80,-50,2))
    m.drawmeridians(range(-180,180,2))
    plt.colorbar(label='Volume (km3)')
    plt.title(u'Volume de temperature T<Tice')
    plt.show()


    plt.gcf().subplots_adjust(left = 0.2, bottom = 0.2, right = 3, top = 3, wspace = 1, hspace = 1)
    plt.show()

    return(h1,h2,h3,h4,h5,h6,latbin,longbin)
