#!/usr/bin/env python
#!/bin/bash

## Calcul des volumes d'air froid (TSTS, TNAT, TICE) sur la période 2007 à 2016.

# Importation modules
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

# Ouverture sortie de modèle CMIP6 de la variable Ta du modèle IPSL sur la période midholocène, possibilité de prendre un autre modèle.
da = xr.open_dataset('ta_Amon_IPSL-CM6A-LR_midHolocene_r1i1p1f2_gr_185001-204912.nc')          

# Extraction de données
ds= da.sel(lat=slice(-80,-50),plev=slice(15000,868))                                          

lat=ds.lat
lon=ds.lon
lev=ds.plev
ta=ds.ta
time=ds.time

latbin=lat.values
longbin=lon.values

# Définition des conditions de températures seuils
Tsts=192
Tnat=195.7
Tice=188

Vsts=np.zeros([120, len(latbin),len(longbin)])
Vnat=np.zeros([120, len(latbin),len(longbin)])
Vice=np.zeros([120, len(latbin),len(longbin)])

month=np.arange(0,120,1)

month=month.reshape((10,12))

for k in range(10):
    for j in range(len(month[k])):
        time=month[k][j]
        print(time)
        idx1 = (ta[time,:,:,:] <= Tsts)
        idx2 = (ta[time,:,:,:] <= Tnat)
        idx3 = (ta[time,:,:,:] <= Tice)
        
        #S vaut 39 120 km carre
        S=141*277.5
        
        lev_km=[3.2,2.7,2.5,3.9,3.1,5.3, 5.4]   #DeltaZ (altitude) entre 14km et 40.6km

        for i in range(24):
            for j in range(144):
                Vsts[time,i,j]=(idx1[:,i,j]*lev_km).sum()*S
                Vnat[time,i,j]=(idx2[:,i,j]*lev_km).sum()*S
                Vice[time,i,j]=(idx3[:,i,j]*lev_km).sum()*S

# Création des fichiers netcdf contenant les volumes TSTS, TNAT, TICE
time=np.arange(0, 120, 1)
STS = xr.DataArray(Vsts[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
NAT = xr.DataArray(Vnat[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
ICE = xr.DataArray(Vice[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})

vol = xr.Dataset({'VTsts':STS,'VTnat':NAT,'VTice':ICE})
vol.to_netcdf('VolT_IPSL_2007_2016.nc')
