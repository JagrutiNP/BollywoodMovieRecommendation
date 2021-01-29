# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:00:09 2020

@author: 10644430
"""


from readParticularMovie_IMDBPage import read_website
import re

class extractMovieVoters():
    def movieVoters(movieID):
        bs=read_website.readFullWebpageread_webpage(movieID)
        voterCount=bs.find('span',itemprop="ratingCount")
        extractVoterCount=re.search('\d+((\,?\d+)*)?',str(voterCount))
        if extractVoterCount:
            totalVoters=extractVoterCount.group()
            totalvoters=int(totalVoters.replace(',', ''))
        else:
            totalvoters=0
        return(totalvoters)
    
# a=extractMovieVoters.movieVoters('tt1603862')
# print(a)
    
