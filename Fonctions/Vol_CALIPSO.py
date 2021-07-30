#!/usr/bin/env python
from Fonctions import Fctyears

years=[2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

for i, year in enumerate(years):
        print(i, year)
        y = Fctyears.volume_season(year)
