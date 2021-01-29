# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:31:44 2020

@author: 10644430
"""
from data_PreProcessing import data_PreProcessing
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
import operator


data=pd.read_excel('D:\work\Movie_Recommendation\Movie_Recommendation\completeData.xlsx')
yearlyMovieCount=data.year_of_release.value_counts(dropna=False).sort_index()
data=data_PreProcessing.dataPrecessing1_genres(data)
data=data_PreProcessing.dataPreprocessing2_actor(data)
data=data_PreProcessing.dataPreprocessing2_director(data)
data=data_PreProcessing().dataPreprocessing3_combinedata(data)
#docTermMatrix=data_PreProcessing().docTermMatrix(data['CombinedData'].tolist())
#docTermMatrix=data_PreProcessing().docTermMatrix(data)
data=data_PreProcessing().preprocessing5(data)
movieNameDict=data_PreProcessing.movieNameDic(data)
identifyMovieIndex=data_PreProcessing.givenMovieIndex(movieNameDict)
cosineSimilarity=data_PreProcessing.cosineSimilarity(data,identifyMovieIndex)

data['top5Movies']=''
for i1 in data.index:
    cosSimDict={}
    print(i1)
    for i2 in data.index:
        cosScore=cosine_similarity(data['DocTermMat'][i1],data['DocTermMat'][i2])
        cosSimDict[data['title'][i2]]=cosScore
    sorted_cosSimilarityDict=dict(sorted(cosSimDict.items(), key=operator.itemgetter(1),reverse=True))
    top6MoviesIndex_SimScore=dict(list(sorted_cosSimilarityDict.items())[1:6])
    top6MoviesIndexlist=list(top6MoviesIndex_SimScore.keys())
    data.top5Movies[i1]=top6MoviesIndexlist
    
    
data['actor11']=data.actor1.replace('\s+', '', regex=True)
MovieRecommendationData.to_excel('D:\work\Movie_Recommendation\Movie_Recommendation\MovieRecommendationData.xlsx', index = False)  

data.top5Movies.apply(pd.Series)



lst_col = 'top5Movies'
import numpy as np

MovieRecommendationData = pd.DataFrame({
      col:np.repeat(data[col].values, data[lst_col].str.len())
      for col in data.columns.drop(lst_col)}
    ).assign(**{lst_col:np.concatenate(data[lst_col].values)})[data.columns]