#!/usr/bin/env python
import xarray as xr
import numpy as np

def grid_points(latsize, lonsize, n, idx, lat, long):
    
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
       350. , 352.5, 355. , 357.5, 360]
    mapV=np.zeros([len(latbin),len(longbin)])
    
    if idx.sum()>0:
        x1=lat[idx].values                                 
        y1=long[idx].values
        n1=n[idx]
    
        for i,latk in enumerate(latbin[:-1]):
            for j,lonj in enumerate(longbin[:-1]):
                idx=(x1 >= latk) & (x1 < (latk+latsize)) & (y1 >= lonj) & (y1 < (lonj+lonsize))
                mapV[i,j]=n1[idx].sum()*0.180*5*0.09

    return mapV


def map_volume(filemonth,latsize,lonsize):
    try:
        data=xr.open_dataset(filemonth)
    except:
        print('probleme ouverture fichier', filemonth)
        return None 
    
    lat=data.Latitude
    long=data.Longitude
    T=data.Temperature
    compo=data.PSC_Composition 
    mask=data.PSC_Feature_Mask
    
    idx=(long<0)
    long[idx]=long[idx]+360.
    

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
       350. , 352.5, 355. , 357.5, 360]
    
    idx=((compo.values==1).sum(axis=1)>0)&(mask.values>200).sum(axis=1)>0
    nsts=((compo.values==1).sum(axis=1))
    mapVsts=grid_points(latsize, lonsize, nsts, idx, lat, long) 
    
    idx=((T.values<192).sum(axis=1)>0)&((mask.values>200).sum(axis=1)>0)
    Tsts=((T.values<192).sum(axis=1))
    mapvTsts=grid_points(latsize, lonsize, Tsts, idx, lat, long)
    if mapvTsts is None:
        mapvTsts=np.zeros([len(latbin),len(longbin)])
    
    c=((compo.values==2)|(compo.values==3)|(compo.values==5))                        
    idx=(c.sum(axis=1)>0)&((mask.values>200).sum(axis=1)>0)
    nnat=(c.sum(axis=1))
    mapVnat=grid_points(latsize, lonsize, nnat, idx, lat, long)
    
    idx=((T.values<195.7).sum(axis=1)>0)&((mask.values>200).sum(axis=1)>0)
    Tnat=((T.values<195.7).sum(axis=1))
    mapvTnat=grid_points(latsize, lonsize, Tnat, idx, lat, long)
    if mapvTnat is None:
        mapvTnat=np.zeros([len(latbin),len(longbin)])
    
    c=((compo.values==4)|(compo.values==6))                        
    idx=(c.sum(axis=1)>0)&((mask.values>200).sum(axis=1)>0)
    nice=(c.sum(axis=1))
    mapVice=grid_points(latsize, lonsize, nice, idx, lat, long)
    
    idx=((T.values<188.5).sum(axis=1)>0)&((mask.values>200).sum(axis=1)>0)
    Tice=((T.values<188.5).sum(axis=1))
    mapvTice=grid_points(latsize, lonsize, Tice, idx, lat, long)
    if mapvTice is None:
        mapvTice=np.zeros([len(latbin),len(longbin)])
        
    data.close()
    
    return(mapVsts,mapvTsts,mapVnat,mapvTnat,mapVice,mapvTice)
