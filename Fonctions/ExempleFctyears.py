#!/usr/bin/env python
import glob
import Fct6V
import FctProf
import numpy as np 
import xarray as xr


year_list=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
month_list=[1,2,3,4,5,6,7,8,9,10,11,12]

for k in year_list:
    for j in month_list:
        Fctmonth.main(year,month)
        
        
        
def main(year='2016', month='1'):
    print(year, month)
    year = int(year)
    month = int(month)
    
    latsize,lonsize=2,15 
    
    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)

    mSTS1 = np.zeros([1, len(latbin),len(longbin)])
    mTsts1= np.zeros([1, len(latbin),len(longbin)])
    mNAT1=np.zeros([1, len(latbin),len(longbin)])
    mTnat1=np.zeros([1, len(latbin),len(longbin)])
    mICE1=np.zeros([1, len(latbin),len(longbin)])
    mTice1=np.zeros([1, len(latbin),len(longbin)])
    mprofils1=np.zeros([1, len(latbin),len(longbin)])

    maps7 = volume_month(year, month, latsize=2, lonsize=15)
    mSTS1[month-1,:,:] = maps7[0]
    mTsts1[month-1,:,:] = maps7[1]
    mNAT1[month-1,:,:] = maps7[2]
    mTnat1[month-1,:,:] = maps7[3]
    mICE1[month-1,:,:] = maps7[4]
    mTice1[month-1,:,:] = maps7[5]
    mprofils1[month-1,:,:]=maps7[6]
    
    time=['%04d-%02d-01' % (year, month)]
    
    mSTSx = xr.DataArray(mSTS1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    mTstsx= xr.DataArray(mTsts1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    mNATx = xr.DataArray(mNAT1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    mTnatx= xr.DataArray(mTnat1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    mICEx= xr.DataArray(mICE1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    mTicex= xr.DataArray(mTice1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    mprofilx= xr.DataArray(mprofils1, dims=('time', 'lat', 'long'), coords={'time':time, 'lat':latbin, 'long':longbin})
    
    data = xr.Dataset({'mSTS':mSTSx,'mTsts':mTstsx,'mNAT':mNATx,'mTnat':mTnatx,'mICE':mICEx, 'mTice':mTicex, 'mprofils':mprofilx})
    outname = '../netcdf/%d_%02d.nc' % (year, month)
    print('Saving ' + outname)
    data.to_netcdf(outname)
    
if __name__=='__main__':
    import plac
    plac.call(main)
