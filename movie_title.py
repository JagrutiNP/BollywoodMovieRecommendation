# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:21:58 2020

@author: 10644430
"""
import re
import requests
from bs4 import BeautifulSoup
from readParticularMovie_IMDBPage import read_website

class movie_title():
    def findTitle(movieId):
        soup=read_website.readFullWebpageread_webpage(movieId)
        title = soup.find_all('title')
        for x in title:
            Ftitle=re.sub('\\s*\\(\\d+\\)\\s\\-\\sIMDb','',x.text)
        return(Ftitle)
# movieTitle=movie_title.findTitle('tt10463030')
# print(movieTitle)