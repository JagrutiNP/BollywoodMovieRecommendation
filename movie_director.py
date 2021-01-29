# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:14:41 2020

@author: 10644430
"""


#find movie director name

from readParticularMovie_IMDBPage import read_website
import re
import numpy as np
import logging


class movie_director():
    def director (movieId):
        bs=read_website.readFullWebpageread_webpage(movieId)
        object =bs.find_all('div', class_='credit_summary_item')
        DirectorNameLine=re.findall('<h4 class="inline">Director?:<\/h4>(.*)<div class="credit_summary_item">',str(object),re.MULTILINE | re.IGNORECASE | re.DOTALL)
        DirectorNameString=re.search('<a href(.*)</a> </div>',str(DirectorNameLine[0]),re.IGNORECASE | re.DOTALL)
        DirectorName=re.search(">([A-Z(a-z)+\s*(A-Z(a-z)+\s)*]+)<|>([A-Za-z]+(\s?\.?[A-Za-z+]\.?\s?)*[A-Za-z]+)<", DirectorNameString.group(), re.IGNORECASE | re.DOTALL)
        return(DirectorName.group(1))


