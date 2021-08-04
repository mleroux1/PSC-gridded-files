#!/usr/bin/env python

## Calcul le nombre de particule NAT en dessous de la troposphère, donc quantifie la dénitrification.

# Importation des modules
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def denitri(filesmonth,latsize,lonsize):
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
    NAT=np.zeros((len(lat),121))                                   # Dans les produits PSC CALIPSO lv2, variables organisées sur 121 niveaux d'altitudes et plusieurs profils (len(lat)).

    # Définition des conditions
    idx=((mask.values<200)&(mask.values>=100))                     # On se place en dessous de la troposphère avec nuages détectés.
    jdx=((compo.values==2)|(compo.values==3)|(compo.values==5))    # On spécifie qu'on veut un PSC NAT

    for k in range(len(lat)):
        for j in range(121):
            if idx[k,j]==jdx[k,j]==True:                           # Si mes deux conditions sont vérifiées, mettre 1 dans la matrice sinon 0
                NAT[k,j]=1
            else:
                NAT[k,j]=0
                
    # On récupère les latitudes et longitudes qui vérifient nos conditions
    a=np.where(NAT==1) 
    l=lat[a[0]].values
    L=long[a[0]].values
    
    # On regarde quelles latitudes et longitudes tombent dans nos mailles
    for i,latk in enumerate(latbin):
        idx=(l>latk)&(l<(latk+latsize))
        if idx.sum()==0:
            continue
        for j,lonj in enumerate(longbin):
            jdx=(L>lonj)&(L<(lonj+lonsize))&idx
            map_den[i,j]=jdx.sum()
            
    # Transformation des points en volumes        
    map_den=[i*0.180*0.09*5 for i in map_den]
            
    data.close()   
    return(map_den)

