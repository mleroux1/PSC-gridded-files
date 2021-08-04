#!/usr/bin/env python
#!/bin/bash


## Calcul des volumes d'air froid (T<TSTS, T<TNAT, T<TICE)

# Importation des modules
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

# Ouverture sortie de modèle avec extraction de données déjà faites par une fonction auparavant, possibilité de le faire ici avec la sélection qui nous intéresse.
ds = xr.open_dataset("/home/mleroux/qsub/IPSL-CM6/SortieTa_extract_ipsl.nc")        #Choisir la sortie de modèle qu'on veut ici, pour avoir la variable Ta.

lat=ds.lat
lon=ds.lon
lev=ds.plev
ta=ds.ta
time=ds.time

latbin=lat.values
longbin=lon.values

# Définition des températures seuils
Tsts=192
Tnat=195.7
Tice=188

# Matrice 3D (time (month), latitudes, longitudes)
Vsts=np.zeros([1032, len(latbin),len(longbin)])
Vnat=np.zeros([1032, len(latbin),len(longbin)])
Vice=np.zeros([1032, len(latbin),len(longbin)])

# Définition du temps, vecteur 1D puis matrice 2D (12 mois par 86 années (2101-2015))
month=np.arange(0,1032,1)

month=month.reshape((86,12))

# Matrice remplie de True/False suivant si la condition est vérifiée ou non.
for k in range(86):
    for j in range(len(month[k])):
        time=month[k][j]
        print(time)
        idx1 = (ta[time,:,:,:] <= Tsts)
        idx2 = (ta[time,:,:,:] <= Tnat)
        idx3 = (ta[time,:,:,:] <= Tice)
        
        #S vaut 39 120 km carre, surface d'une maille.
        S=141*277.5
        
        lev_km=[3.2,2.7,2.5,3.9,3.1,5.3,5.4]                          #DeltaZ (altitude en km) entre 14km et 40.6km

        for i in range(24):                                           #Parcours des deltas latitudes 
            for j in range(144):                                      #Parcours des deltas longitudes 
                Vsts[time,i,j]=(idx1[:,i,j]*lev_km).sum()*S
                Vnat[time,i,j]=(idx2[:,i,j]*lev_km).sum()*S
                Vice[time,i,j]=(idx3[:,i,j]*lev_km).sum()*S

# Création des fichiers netcdf contenant les volumes TSTS, TNAT, TICE
time=np.arange(0, 1032, 1)
STS = xr.DataArray(Vsts[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
NAT = xr.DataArray(Vnat[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
ICE = xr.DataArray(Vice[:,:,:], dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})

vol = xr.Dataset({'VTsts':STS,'VTnat':NAT,'VTice':ICE})
vol.to_netcdf('VolT_IPSL_2015_2100.nc')
              
