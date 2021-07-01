# Regridage
## Regarder combien de maille du modèle (1.27x2.5)tombe dans une maille de CALI (2x15)

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

ds = xr.open_dataset("/home/mleroux/Vol_CALI/10years.nc")
da = xr.open_dataset("/home/mleroux/qsub/VOL_IPSL.nc")



