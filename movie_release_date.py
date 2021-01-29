# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:05:29 2020

@author: 10644430
"""


from readParticularMovie_IMDBPage import read_website
import re

class movie_release_year():
    def movie_release_Year(movieId):
        bs=read_website.readFullWebpageread_webpage(movieId)
        v=re.search('\d{4}',str(bs.find('title')))
        return v.group()
# b=movie_release_year.movie_release_Year('tt0189592')
# print(b)
    

    def movie_release_date(movieId):
        bs=read_website.readFullWebpageread_webpage(movieId)
        parse_releaseDate = bs.find_all('a')
        findReleaseDate=re.search('\d+\s+[A-Z][a-z]+\s+\d{4}(\s*\([[A-Za-z]+\))?',str(parse_releaseDate))
        if findReleaseDate:
            MovieReleaseDate=findReleaseDate.group()
        else:
            MovieReleaseDate=0
        #parse_releaseDate=bs.find_all('a href',{'title':"see more release dates"})
        return(MovieReleaseDate)
    
#print(movie_release_year.movie_release_date('tt0364519'))


