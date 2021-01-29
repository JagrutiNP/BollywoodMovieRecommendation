# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:39:06 2020

@author: 10644430
"""

import pandas as pd
import os
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import imdb 
from readParticularMovie_IMDBPage import read_website

## read excel file
def readExcel(foldername,filename):
    data=pd.read_csv(foldername+'\\'+filename)
    return(data)

def removeNan(dataframe):
    data = dataframe[dataframe['imdb_id'].notna()]
    return(data)

def writeDF(dfPath,df):
    df.to_csv (dfPath+'\\'+'combine_dataframe.csv', index = False, header=True)

def fillNATitle(dataframe):
    nan_rows = dataframe[dataframe['title_x'].isna()]
    return(nan_rows)
      

bollywood=readExcel('D:/work/Movie_Recommendation/Movie_Recommendation/TIMDB-master/1950-1989','bollywood.csv')
bollywood=removeNan(bollywood)
bollywood_meta=readExcel('D:\work\Movie_Recommendation\Movie_Recommendation\TIMDB-master\1950-1989','bollywood_meta.csv')
bollywood_meta=removeNan(bollywood_meta)
bollywood_ratings=readExcel('D:\work\Movie_Recommendation\Movie_Recommendation\1950-1989','bollywood_ratings.csv')
bollywood_ratings=removeNan(bollywood_ratings)
bollywood_text=readExcel('D:\work\Movie_Recommendation\Movie_Recommendation\1950-1989','bollywood_text.csv')
bollywood_text=removeNan(bollywood_text)
merge_1=bollywood.merge(bollywood_meta,on='imdb_id',how='outer').merge(bollywood_ratings,on='imdb_id',how='outer').merge(bollywood_text,on='imdb_id',how='outer')
missingTitle=fillNATitle(merge_1)
if missingTitle.empty ==True:
    pass
else:
    print('no')
combine1=writeDF('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_1950-1989',merge_1)


bollywood=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_1990-2009','bollywood.csv')
bollywood=removeNan(bollywood)
bollywood_meta=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_1990-2009','bollywood_meta.csv')
bollywood_meta=removeNan(bollywood_meta)
bollywood_ratings=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_1990-2009','bollywood_ratings.csv')
bollywood_ratings=removeNan(bollywood_ratings)
bollywood_text=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_1990-2009','bollywood_text.csv')
bollywood_text=removeNan(bollywood_text)
merge_2=bollywood.merge(bollywood_meta,on='imdb_id',how='outer').merge(bollywood_ratings,on='imdb_id',how='outer').merge(bollywood_text,on='imdb_id',how='outer')
missingTitle=fillNATitle(merge_2)
if missingTitle.empty ==True:
    pass
else:
    print('no')
combine1=writeDF('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_1990-2009',merge_2)

bollywood=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_2010-2019','bollywood.csv')
bollywood=removeNan(bollywood)
bollywood_meta=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_2010-2019','bollywood_meta.csv')
bollywood_meta=removeNan(bollywood_meta)
bollywood_ratings=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_2010-2019','bollywood_ratings.csv')
bollywood_ratings=removeNan(bollywood_ratings)
bollywood_text=readExcel('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_2010-2019','bollywood_text.csv')
bollywood_text=removeNan(bollywood_text)
merge_3=bollywood.merge(bollywood_meta,on='imdb_id',how='outer').merge(bollywood_ratings,on='imdb_id',how='outer').merge(bollywood_text,on='imdb_id',how='outer')
combine1=writeDF('D:\Jagruti\MovieRecommendation\TIMDB-master\Folder_2010-2019',merge_3)





