#!/usr/bin/env python
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

def nb_inf_tropo(nom_fichier,latsize,lonsize):

    data=xr.open_dataset(nom_fichier,engine='pynio')
    lat=data.Latitude
    long=data.Longitude
    compo=data.PSC_Composition 
    mask=data.PSC_Feature_Mask

    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)

    map_nb_tot=np.zeros([len(latbin),len(longbin)])
    nb_tot=np.zeros((len(lat),121))

    idx=((mask.values<200)&(mask.values>=100))   

    for k in range(len(lat)):
        for j in range(121):
            if idx[k,j]==True:
                nb_tot[k,j]+=1
            else:
                nb_tot[k,j]=0

    a=np.where(nb_tot==1) 
    l=lat[a[0]].values
    L=long[a[0]].values

    for i,latk in enumerate(latbin):
        idx=(l>latk)&(l<(latk+2))
        if idx.sum()==0:
            continue
        for j,lonj in enumerate(longbin):
            jdx=(L>lonj)&(L<(lonj+15))&idx
            map_nb_tot[i,j]=jdx.sum()
            
    data.close()   
    return(map_nb_tot) 