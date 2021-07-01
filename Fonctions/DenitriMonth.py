#!/usr/bin/env python
import glob
from Fonctions import Denitri
from Fonctions import Nbinftropo
import numpy as np 
import xarray as xr

def denitrification_month(year, month, latsize=2, lonsize=15):
    filesmonth=sorted(glob.glob('/bdd/CALIPSO/Lidar_L2/LID_L2_PSCMask-Prov-V1-00/%04d/%02d/*.hdf' % (year, month)))

    if len(filesmonth)==0:
        print('No files')

    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)

    nbNAT=np.zeros([len(latbin),len(longbin)])
    nbTOT=np.zeros([len(latbin),len(longbin)])

    for k in range(len(filesmonth)):
        
        if k % 2 == 0:
            print('file #%02d/%02d' % (k, len(filesmonth)))
        
        y=Denitri.denitrification(filesmonth[k],2,15)
        if y is None:
            continue

        nbNAT=nbNAT+y

 
    return(nbNAT)
