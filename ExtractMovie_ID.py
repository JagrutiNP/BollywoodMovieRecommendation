# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:30:26 2020

@author: 10644430
"""

import imdb 
import re

# class fetchMovieId():
#     def MovieId (moviename):
#         ## get access of imdb data using python
#         ia = imdb.IMDb() 
#         if re.search ('\d+\s*film',moviename):
#             moviename=moviename.replace(' film','')
            
#         else:
#             moviename=moviename
#         search = ia.search_movie(moviename) 
#         movieId=re.search ('\d+',str(search), re.M|re.S)
#         movieID='tt'+str(movieId.group())
#         return(movieID)
# # a=fetchMovieId.MovieId('Bahurani (1989 film)')
# # print(a)

class fetchMovieId():
    def MovieId (moviename):
        ## get access of imdb data using python
        ia = imdb.IMDb() 
        year_film=re.search ('\d+\s*film',moviename)
        if year_film:
            #moviename=moviename.replace(' film|\(film\)','')
            moviename=re.sub(' film|\(film\)','',year_film.group())
            
        # else:
        #     moviename=moviename
        # print(moviename,'++++++++')
        search = ia.search_movie(moviename) 
        movieId=re.search ('\d+',str(search), re.M|re.S)
        movieID='tt'+str(movieId.group())
        return(movieID)
# a=fetchMovieId.MovieId('Tum Mere Ho')
# print(a)