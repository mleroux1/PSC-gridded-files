#!/usr/bin/env python
#!/bin/bash

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

## Calcul des volumes d'air froid (TSTS, TNAT, TICE)

ds = xr.open_dataset("/home/mleroux/qsub/IPSL-CM6/SortieTa_extract_ipsl.nc")

lat=ds.lat
lon=ds.lon
lev=ds.plev
ta=ds.ta
time=ds.time

latbin=lat.values
longbin=lon.values

Tsts=192
Tnat=195.7
Tice=188

Vsts=np.zeros([1032, len(latbin),len(longbin)])
Vnat=np.zeros([1032, len(latbin),len(longbin)])
Vice=np.zeros([1032, len(latbin),len(longbin)])

month=np.arange(0,1032,1)

month=month.reshape((86,12))

for k in range(86):
    for j in range(len(month[k])):
        time=month[k][j]
        print(time)
        idx1 = (ta[time,:,:,:] <= Tsts)
        idx2 = (ta[time,:,:,:] <= Tnat)
        idx3 = (ta[time,:,:,:] <= Tice)
        
        #S vaut 39 120 km carre
        S=141*277.5
        
        lev_km=[3.2,2.7,2.5,3.9,3.1,5.3,5.4]   #DeltaZ (altitude) entre 14km et 40.6km

        for i in range(24):
            for j in range(144):
                Vsts[time,i,j]=(idx1[:,i,j]*lev_km).sum()*S
                Vnat[time,i,j]=(idx2[:,i,j]*lev_km).sum()*S
                Vice[time,i,j]=(idx3[:,i,j]*lev_km).sum()*S
                
time=np.arange(0, 1032, 1)
STS = xr.DataArray(Vsts[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
NAT = xr.DataArray(Vnat[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
ICE = xr.DataArray(Vice[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})

vol = xr.Dataset({'VTsts':STS,'VTnat':NAT,'VTice':ICE})
vol.to_netcdf('VolT_IPSL_2015_2100.nc')
              
