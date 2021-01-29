# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:55:24 2020

@author: 10644430
"""


from readParticularMovie_IMDBPage import read_website
import re

class movie_Genres():
    def findGenres(movieId):
        bs=read_website.readFullWebpageread_webpage(movieId)
        genre_sent=bs.select("a[href*=genres]")
        genreList=[]
        for sent in genre_sent:
            genre=re.search(r'\>\s*([A-Za-z\d]+)\<',str(sent),re.S|re.M)
            if genre:
                genreList.append(genre.group(1))
        uniqueGenreList=set(genreList)
        genres = '|'.join([str(elem) for elem in uniqueGenreList]) 
        return(genres)
    
# genre= movie_Genres.findGenres('tt0254481')
# print(genre)
