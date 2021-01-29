# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:51:22 2020

@author: 10644430
"""

from readParticularMovie_IMDBPage import read_website
import re
import requests
import io
from PIL import Image


class moviePoster():
    def findPoster(movieId):
        print(movieId)
        bs=read_website.readFullWebpageread_webpage(movieId)
        images = bs.find_all('img', {'src':re.compile('.jpg')})
        print(images)
        if len(images)>0:
            for image in images: 
                posterPath=image['src']
                break
            if posterPath==None:
                PathOfPoster=0
            else:
                PathOfPoster=posterPath
                response = requests.get(PathOfPoster,verify=False)
                image_bytes = io.BytesIO(response.content)
                img = Image.open(image_bytes)
    #        img.show()
            return PathOfPoster
        else:
            return 'No Poster Image'
        
a=moviePoster.findPoster('tt1961530')
print(a)
    



                   

