#!/usr/bin/env python
import xarray as xr
import numpy as np

def grid_points(latsize, lonsize, n, idx, lat, long):
    
    latbin=np.arange(-80,-50+2,latsize)
    longbin=np.arange(-180,180+15,lonsize)
    mapV=np.zeros([len(latbin),len(longbin)])
    
    if idx.sum()>0:
        x1=lat[idx].values                                 
        y1=long[idx].values
        n1=n[idx]
    
        for i,latk in enumerate(latbin[:-1]):
            for j,lonj in enumerate(longbin[:-1]):
                idx=(x1 >= latk) & (x1 < (latk+latsize)) & (y1 >= lonj) & (y1 < (lonj+lonsize))
                mapV[i,j]=n1[idx].sum()*0.180*5*0.09

    return mapV


def map_volume(filemonth,latsize,lonsize):
    try:
        data=xr.open_dataset(filemonth)
    except:
        print('probleme ouverture fichier', filemonth)
        return None 
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
    if mapvTsts is None:
        mapvTsts=np.zeros([len(latbin),len(longbin)])
    
    c=((compo.values==2)|(compo.values==3)|(compo.values==5))                        
    idx=(c.sum(axis=1)>0)
    nnat=(c.sum(axis=1))
    mapVnat=grid_points(latsize, lonsize, nnat, idx, lat, long)
    
    idx=((T.values<195.7).sum(axis=1)>0)
    Tnat=((T.values<195.7).sum(axis=1))
    mapvTnat=grid_points(latsize, lonsize, Tnat, idx, lat, long)
    if mapvTnat is None:
        mapvTnat=np.zeros([len(latbin),len(longbin)])
    
    c=((compo.values==4)|(compo.values==6))                        
    idx=(c.sum(axis=1)>0)
    nice=(c.sum(axis=1))
    mapVice=grid_points(latsize, lonsize, nice, idx, lat, long)
    
    idx=((T.values<188.5).sum(axis=1)>0)
    Tice=((T.values<188.5).sum(axis=1))
    mapvTice=grid_points(latsize, lonsize, Tice, idx, lat, long)
    if mapvTice is None:
        mapvTice=np.zeros([len(latbin),len(longbin)])
        
    data.close()
    
    return(mapVsts,mapvTsts,mapVnat,mapvTnat,mapVice,mapvTice)
    
