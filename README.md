# StagePSC

##Volumes de PSC et d'air froid

Les fonctions Fct6V_CALI et Fct6V_CMIP6 servent à calculer des volumes journaliers de PSC (STS, NAT, ICE) et de température (TSTS, TNAT, TICE) à partir de fichiers hdf. La différence entre les deux est la dimension des mailles spatiales. Pour CALIPSO: 2°x15°, pour CMIP6: 1.27°x2.5°
On peut ensuite calculer des volumes mensuels et annuels à l'aide des fonctions Fctmonth et fctyears. 
Si on veut des volumes moyens par profils, il faudra faire appel à la fonction FctProf qui calcule le nombre de profils CALIPSO tombant dans une maille.

## Dénitrification

La fonction Denitri permet de calculer 
