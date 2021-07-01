import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


def histogram_volume(nom_fichier,latsize,lonsize):
    data=xr.open_dataset(nom_fichier,engine='pynio')
    lat=data.Latitude
    long=data.Longitude
    T=data.Temperature
    compo=data.PSC_Composition 

    latbin=range(-80,-50+2,latsize)
    longbin=range(-180,180+15,lonsize)


    mapVsts=np.zeros([len(latbin)-1,len(longbin)-1])

    idx=((compo.values==1).sum(axis=1))>0
    nsts=((compo.values==1).sum(axis=1))
    x1=lat[idx].values                                  
    y1=long[idx].values
    n1=nsts[idx]

    subplot(3,3,1)
   
    h1, xx, yy = np.histogram2d(x1, y1, (latbin, longbin), weights=n1)
    h1 *= (0.180*5*0.9)
    plt.pcolormesh(h1)
    plt.colorbar(label='Volume (km3)')
    xlabel('Longitude')
    ylabel('Latitude')
    plt.title('Volume de STS')
 



    idx=((T.values<192).sum(axis=1)>0)
    Tsts=((T.values<192).sum(axis=1))

    mapvTsts=np.zeros([len(latbin)-1,len(longbin)-1])
    x1=lat[idx].values                                                     
    y1=long[idx].values
    T1=Tsts[idx]

    subplot(3,3,2)
  
    h2, xx, yy = np.histogram2d(x1, y1, (latbin, longbin), weights=T1)
    h2 *= (0.180*5*0.9)
    plt.pcolormesh(h2)
    plt.colorbar(label='Volume (km3)')
    xlabel('Longitude')
    ylabel('Latitude')
    plt.title(u'Volume de temperature T<Tsts')
  


    c=((compo.values==2)|(compo.values==3)|(compo.values==5))                        
    idx=(c.sum(axis=1)>0)
    nnat=(c.sum(axis=1))

    mapVnat=np.zeros([len(latbin),len(longbin)])
    x2=lat[idx].values
    y2=long[idx].values
    n2=nnat[idx]

    subplot(3,3,3)
    
    h3, xx, yy = np.histogram2d(x2, y2, (latbin, longbin), weights=n2)
    h3 *= (0.180*5*0.9)
    plt.pcolormesh(h3)
    plt.colorbar(label='Volume (km3)')
    xlabel('Longitude')
    ylabel('Latitude')
    plt.title('Volume de NAT')
   


    idx=((T.values<195.7).sum(axis=1)>0)
    Tnat=((T.values<195.7).sum(axis=1))

    mapvTnat=np.zeros([len(latbin)-1,len(longbin)-1])
    x2=lat[idx].values                                                   
    y2=long[idx].values
    T2=Tnat[idx]

    subplot(3,3,4)

    h4, xx, yy = np.histogram2d(x2, y2, (latbin, longbin), weights=T2)
    h4 *= (0.180*5*0.9)
    plt.pcolormesh(h4)
    plt.colorbar(label='Volume (km3)')
    xlabel('Longitude')
    ylabel('Latitude')
    plt.title(u'Volume de temperature T<Tnat')
  


    c=((compo.values==4)|(compo.values==6))                        
    idx=(c.sum(axis=1)>0)
    nice=(c.sum(axis=1))
    mapVice=np.zeros([len(latbin),len(longbin)])

    x3=lat[idx].values
    y3=long[idx].values
    n3=nice[idx]

    subplot(3,3,5)

    h5, xx, yy = np.histogram2d(x3, y3, (latbin, longbin), weights=n3)
    h5 *= (0.180*5*0.9)
    plt.pcolormesh(h5)
    plt.colorbar(label='Volume (km3)')
    xlabel('Longitude')
    ylabel('Latitude')
    plt.title('Volume de Ice')
    


    idx=((T.values<188.5).sum(axis=1)>0)
    Tice=((T.values<188.5).sum(axis=1))
    mapvTice=np.zeros([len(latbin)-1,len(longbin)-1])

    x3=lat[idx].values                                             
    y3=long[idx].values
    T3=Tice[idx]

    subplot(3,3,6)

    h6, xx, yy = np.histogram2d(x3, y3, (latbin, longbin), weights=T3)
    h6 *= (0.180*5*0.9)
    plt.pcolormesh(h6)
    plt.colorbar(label='Volume (km3)')
    xlabel('Longitude')
    ylabel('Latitude')
    plt.title(u'Volume de temperature T<Tice')
    
    plt.gcf().subplots_adjust(left = 0, bottom = 0, right = 2, top = 2, wspace = 0.5, hspace = 0.5)
    plt.show()

    return(h1,h2,h3,h4,h5,h6,latbin,longbin)