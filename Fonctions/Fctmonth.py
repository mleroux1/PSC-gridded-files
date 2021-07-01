#!/usr/bin/env python
import glob
from Fonctions import Fct6Vcorrige
from Fonctions import FctProf
import numpy as np 
import xarray as xr

def volume_month(year, month, latsize=1.27, lonsize=2.5):
    filesmonth=sorted(glob.glob('/bdd/CALIPSO/Lidar_L2/LID_L2_PSCMask-Prov-V1-00/%04d/%02d/*.hdf' % (year, month)))

    if len(filesmonth)==0:
        print('No files')

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
    
    vSTS=np.zeros([len(latbin),len(longbin)])
    vTsts=np.zeros([len(latbin),len(longbin)])
    vNAT=np.zeros([len(latbin),len(longbin)])
    vTnat=np.zeros([len(latbin),len(longbin)])
    vICE=np.zeros([len(latbin),len(longbin)])
    vTice=np.zeros([len(latbin),len(longbin)])
    nbp=np.zeros([len(latbin),len(longbin)])


    for k in range(len(filesmonth)):
        
        if k % 2 == 0:
            print('file #%02d/%02d' % (k, len(filesmonth)))
        
        y=Fct6Vcorrige.map_volume(filesmonth[k],1.27,2.5)
        if y is None:
            continue
        x=FctProf.nb_profils(filesmonth[k],1.27,2.5)

        vSTS=vSTS+y[0]
        vTsts=vTsts+y[1]
        vNAT=vNAT+y[2]
        vTnat=vTnat+y[3]
        vICE=vICE+y[4]
        vTice=vTice+y[5]
        nbp=nbp+x
    

    m=[vSTS,vTsts,vNAT,vTnat,vICE,vTice,nbp]
    return(m)


