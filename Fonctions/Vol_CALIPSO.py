#!/usr/bin/env python
from Fonctions import Fctyears

## Fonction pour calculer les volumes de PSC (STS, NAT, ICE) et les volumes d'air froid (T<TSTS, T<TNAT, T<TICE) à partir des observations CALIPSO sur la période 2007 à 2016.

years=[2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

for i, year in enumerate(years):
        print(i, year)
        y = Fctyears.volume_season(year)
