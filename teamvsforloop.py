# -*- coding: utf-8 -*-
"""
Created on Sat May 16 00:58:38 2020

@author: Christina
"""

teams = ['Dragons','Wolves','Pandas','Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + "vs" + away_team)