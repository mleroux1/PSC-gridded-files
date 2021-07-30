#!/usr/bin/env python
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def denitrification(filesmonth,latsize,lonsize):
    try:
        data=xr.open_dataset(filesmonth, engine='pynio')
    except:
        print('probleme ouverture fichier', filesmonth)
        return None 
    lat=data.Latitude
    long=data.Longitude
    compo=data.PSC_Composition 
    mask=data.PSC_Feature_Mask

    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)

    map_den=np.zeros([len(latbin),len(longbin)])
    NAT=np.zeros((len(lat),121))

    idx=((mask.values<200)&(mask.values>=100))   
    jdx=((compo.values==2)|(compo.values==3)|(compo.values==5))

    for k in range(len(lat)):
        for j in range(121):
            if idx[k,j]==jdx[k,j]==True:
                NAT[k,j]=1
            else:
                NAT[k,j]=0

    a=np.where(NAT==1) 
    l=lat[a[0]].values
    L=long[a[0]].values

    for i,latk in enumerate(latbin):
        idx=(l>latk)&(l<(latk+2))
        if idx.sum()==0:
            continue
        for j,lonj in enumerate(longbin):
            jdx=(L>lonj)&(L<(lonj+15))&idx
            map_den[i,j]=jdx.sum()
            
    map_den=[i*0.180*0.09*5 for i in map_den]
            
    data.close()   
    return(map_den)

