#!/usr/bin/env python

## Calcul du nombre de profils CALIPSO tombant dans les mailles du modèle.

# Importation modules
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

def nb_profils(nom_fichier,latsize,lonsize):

    data=xr.open_dataset(nom_fichier)
    lat=data.Latitude
    long=data.Longitude

    latbin=np.arange(-80,-50+2,2)
    longbin=np.arange(-180,180+15,15)
    mapprof=np.zeros([len(latbin),len(longbin)])
    
    # A activer si on travail avec des longitudes non définies entre -180° et 180°, comme avec les sorties de modèles CMIP6
    #idx=(long<0)
    #long[idx]=long[idx]+360.

    x1=lat.values
    y1=long.values

    for i,latk in enumerate(latbin):
        idx=(x1>latk)&(x1<(latk+2))
        if idx.sum()==0:
            continue
        for j,lonj in enumerate(longbin):
            jdx=(y1>lonj)&(y1<(lonj+15))&idx
            mapprof[i,j]=jdx.sum()
            
    data.close()
        
    return(mapprof) 
