# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:12:13 2020

@author: 10644430
"""
from readParticularMovie_IMDBPage import read_website
import re

class extractMovieDuration():
    def movieRunTime(movieID):
        bs=read_website.readFullWebpageread_webpage(movieID)
        timerate = bs.find('time')
        movieDuration=re.search('\d*h\s*\d+min',str(timerate))
        if movieDuration:
            givenMovieDuration=movieDuration.group()
        else:
            givenMovieDuration='Not Mentioned'
        return givenMovieDuration
        # extractMovieRating=re.search('\d+(\.?\d+)?',str(rate))
        # return extractMovieRating.group()
# print(extractMovieRating.group())
# rating_value=bs.find('span',itemprop="ratingCount")
# extractRatingCount=re.search('\d+((\,?\d+)*)?',str(rating_value))
# print(extractRatingCount.group())



    