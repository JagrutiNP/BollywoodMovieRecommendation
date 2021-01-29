# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:39:17 2020

@author: 10644430
"""
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

class read_website():
        
    def readFullWebpageread_webpage (movieId):
        url='https://www.imdb.com/title/'+str(movieId)+'/?ref_=ttpl_pl_tt'
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        bslist=str(bs).split('\n')
        lineNo=[]
        for string in bslist:
            findStr=re.search ('view\sproduction\,\s+box\s+office\, \&amp; company info',string,re.IGNORECASE|re.M|re.S)
            if findStr:
                lineNo.append(bslist.index(findStr.group()))
                if len(lineNo)!=0:
                    break
        bsString='\n'.join(bslist[0:lineNo[0]+1])
        ## convert string to html tags
        ## extract data from web till line view production, box office & company info
        bs=BeautifulSoup(bsString,'html.parser')
        return bs
    
    def readSummaryWebpage (movieId):
        url='https://www.imdb.com/title/'+str(movieId)+'/plotsummary?ref_=tt_stry_pl'
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        return bs
    
#read_website.read_webpage('tt7725596')