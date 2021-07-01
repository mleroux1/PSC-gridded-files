#!/usr/bin/env python

from Fonctions import Fctmonth
from Fonctions import FctProf
import numpy as np
import glob

def volume_season(year):
    month_list=[5,6,7,8,9,10]
    latsize,lonsize=2,15 

    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)

    mSTS = np.zeros([12, len(latbin),len(longbin)])
    mTsts= np.zeros([12, len(latbin),len(longbin)])
    mNAT=np.zeros([12, len(latbin),len(longbin)])
    mTnat=np.zeros([12, len(latbin),len(longbin)])
    mICE=np.zeros([12, len(latbin),len(longbin)])
    mTice=np.zeros([12, len(latbin),len(longbin)])
    mprofils=np.zeros([12, len(latbin),len(longbin)])

    for i, month in enumerate(month_list):
        print(i, month)
        maps7 = Fctmonth.volume_month(year, month, latsize=2, lonsize=15)
        mSTS[month,:,:] = maps7[0]
        mTsts[month,:,:] = maps7[1]
        mNAT[month,:,:] = maps7[2]
        mTnat[month,:,:] = maps7[3]
        mICE[month,:,:] = maps7[4]
        mTice[month,:,:] = maps7[5]
        mprofils[month,:,:]=maps7[6]

    return(mSTS,mTsts,mNAT,mTnat,mICE,mTice,mprofils)


