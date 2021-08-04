#!/usr/bin/env python

## Calcul de la dénitrification mensuel à partir des fichiers hdf journaliers

# Importation des modules et fonctions utiles
from Fonctions import Denitrification
from Fonctions import FctProf
import numpy as np 
import xarray as xr
import glob

def denitrification_month(year, month, latsize, lonsize):
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
        
        y=Denitrification.denitri(filesmonth[k],latsize,lonsize)
        if y is None:
            continue

        nbNAT=nbNAT+y    #Attention si on somme, il va falloir diviser par le nombre de jours (de fichiers) pour normaliser.
 
    return(nbNAT)
