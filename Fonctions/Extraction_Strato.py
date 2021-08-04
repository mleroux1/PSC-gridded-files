# Importation modules
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

# Ouverture du fichiers dont on veut extraire certaines données.
ds = xr.open_dataset("/home/mleroux/ta_Amon_IPSL-CM6A-LR_ssp585_r3i1p1f1_gr_201501-210012.nc") #decode_times=False pour transformer les dates en nombre de seconde ou jours.

# Sélection sur les latitudes et les altitudes (ici en pression).
da= ds.sel(lat=slice(-80,-50),plev=slice(15000,868))               

# Création du nouveau fichier
da.to_netcdf('SortieTa_extract_ipsl.nc')
