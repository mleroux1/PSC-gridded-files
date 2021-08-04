# StagePSC

## Volumes de PSC et d'air froid à partir des observations CALIPSO

Les fonctions Fct6V_CALI et Fct6V_CMIP6 servent à calculer des volumes journaliers de PSC (STS, NAT, ICE) et de température (TSTS, TNAT, TICE) à partir des produits PSC CALIPSO lv2. La différence entre les deux fonctions est la dimension des mailles spatiales (CALI: 2°x15°, CMIP6: 1.27°x2.5°).
On peut ensuite calculer des volumes mensuels et annuels de PSC et d'air froid à l'aide des fonctions Fctmonth et Fctyears. 
Si on veut des volumes moyens par profils, il faudra faire appel à la fonction FctProf qui calcule le nombre de profils CALIPSO tombant dans une maille.

## Dénitrification

La fonction Denitrification permet de calculer des volumes de PSC NAT en dessous de la tropopause, donc de quantifier la dénitrification sur des fichiers hdf journaliers. La fonction Denitrification_Month permet de le faire mensuellement. 

## Sorties de modèles CMIP6

Les fonctions VolT_IPSL_... calculent les volumes d'air froid (T<TSTS, T<TNAT, T<TICE) à partir de la température stratosphérique Ta prédite par les sorties de modèles CMIP6. Il faudra d'ailleurs choisir la sortie de modèle qu'on veut (modèle IPSL, CNRM, etc..); les fonctions VolPSC_modele_... calculent les volumes de PSC (STS, NAT, ICE) à partir des volumes d'air froid calculés par VolT_IPSL_...
