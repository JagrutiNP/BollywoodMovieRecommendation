# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:08:21 2020

@author: 10644430
"""


from readParticularMovie_IMDBPage import read_website
import re

class extractMovieRating():
    def movieRating(movieID):
        bs=read_website.readFullWebpageread_webpage(movieID)
        rate = bs.find('span',itemprop='ratingValue')
        extractMovieRating=re.search('\d+(\.?\d+)?',str(rate))
        return extractMovieRating.group()

# a=extractMovieRating.movieRating('tt1399602')
# print(a)
