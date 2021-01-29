# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:18:55 2020

@author: 10644430
"""
from readParticularMovie_IMDBPage import read_website
import re

class movie_actor():
    def actor (movieId):
        bs=read_website.readFullWebpageread_webpage(movieId)
        ActorNameList=[]
        object =bs.find_all('div', class_='credit_summary_item')
        actorNames=re.finditer ('>(([A-Z][a-z]*\s?)*)<\/a>',str(object[-1]),re.S|re.M|re.I)
        for matchNum, match in enumerate(actorNames):
           ActorNameList.append(match.group(1))
        ActorsNames = '|'.join([str(elem) for elem in ActorNameList]) 
        return ActorsNames
           
# v=movie_actor.actor('tt10443846')
# print(v)

