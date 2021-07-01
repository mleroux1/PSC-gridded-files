#!/usr/bin/env python
from Fonctions import Fctmonth
from Fonctions import FctProf
import xarray as xr
import numpy as np
import glob

def volume_season(year):
    
    month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    latsize,lonsize=(1.27,2.5)

    latbin=[-79.85915 , -78.59155 , -77.323944, -76.056335, -74.788734, -73.521126,
       -72.253525, -70.985916, -69.71831 , -68.45071 , -67.1831  , -65.91549 ,
       -64.64789 , -63.380283, -62.112675, -60.84507 , -59.577465, -58.30986 ,
       -57.042255, -55.774647, -54.507042, -53.239437, -51.971832, -50.704224]
    longbin=[  0. ,   2.5,   5. ,   7.5,  10. ,  12.5,  15. ,  17.5,  20. ,  22.5,
        25. ,  27.5,  30. ,  32.5,  35. ,  37.5,  40. ,  42.5,  45. ,  47.5,
        50. ,  52.5,  55. ,  57.5,  60. ,  62.5,  65. ,  67.5,  70. ,  72.5,
        75. ,  77.5,  80. ,  82.5,  85. ,  87.5,  90. ,  92.5,  95. ,  97.5,
       100. , 102.5, 105. , 107.5, 110. , 112.5, 115. , 117.5, 120. , 122.5,
       125. , 127.5, 130. , 132.5, 135. , 137.5, 140. , 142.5, 145. , 147.5,
       150. , 152.5, 155. , 157.5, 160. , 162.5, 165. , 167.5, 170. , 172.5,
       175. , 177.5, 180. , 182.5, 185. , 187.5, 190. , 192.5, 195. , 197.5,
       200. , 202.5, 205. , 207.5, 210. , 212.5, 215. , 217.5, 220. , 222.5,
       225. , 227.5, 230. , 232.5, 235. , 237.5, 240. , 242.5, 245. , 247.5,
       250. , 252.5, 255. , 257.5, 260. , 262.5, 265. , 267.5, 270. , 272.5,
       275. , 277.5, 280. , 282.5, 285. , 287.5, 290. , 292.5, 295. , 297.5,
       300. , 302.5, 305. , 307.5, 310. , 312.5, 315. , 317.5, 320. , 322.5,
       325. , 327.5, 330. , 332.5, 335. , 337.5, 340. , 342.5, 345. , 347.5,
       350. , 352.5, 355. , 357.5]

    mSTS = np.zeros([1, len(latbin),len(longbin)])
    mTsts= np.zeros([1, len(latbin),len(longbin)])
    mNAT=np.zeros([1, len(latbin),len(longbin)])
    mTnat=np.zeros([1, len(latbin),len(longbin)])
    mICE=np.zeros([1, len(latbin),len(longbin)])
    mTice=np.zeros([1, len(latbin),len(longbin)])
    mprofils=np.zeros([1, len(latbin),len(longbin)])

    for i, month in enumerate(month_list):
        print(i, month)
        maps7 = Fctmonth.volume_month(year, month, latsize=1.27, lonsize=2.5)
        mSTS[0,:,:] = maps7[0]
        mTsts[0,:,:] = maps7[1]
        mNAT[0,:,:] = maps7[2]
        mTnat[0,:,:] = maps7[3]
        mICE[0,:,:] = maps7[4]
        mTice[0,:,:] = maps7[5]
        mprofils[0,:,:]=maps7[6]

        time=['%04d-%02d' % (year, month)]
    
        mSTSx = xr.DataArray(mSTS, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
        mTstsx= xr.DataArray(mTsts, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
        mNATx = xr.DataArray(mNAT, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
        mTnatx= xr.DataArray(mTnat, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
        mICEx= xr.DataArray(mICE, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
        mTicex= xr.DataArray(mTice, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
        mprofilx= xr.DataArray(mprofils, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    
        data = xr.Dataset({'vol_STS':mSTSx,'vol_Tsts':mTstsx,'vol_NAT':mNATx,'vol_Tnat':mTnatx,'vol_ICE':mICEx, 'vol_Tice':mTicex, 'nb_profils':mprofilx})
        data.to_netcdf('%d_%02d.nc' % (year, month))

if __name__=='__main__':
    import plac
    plac.call(main)