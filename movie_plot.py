# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:44:22 2020

@author: 10644430
"""

import re
from readParticularMovie_IMDBPage import read_website

#+++++++++++++++++++++++++++++++extract plot+++++++++++++++++++++++++++++

class extractPlot():
    def extractStoryPlot(movieId):
        bs=read_website.readSummaryWebpage(movieId)
        plot_parse_list=bs.find_all('li',{'class':"ipl-zebra-list__item"})
        if len(plot_parse_list)!=0:
            if len(plot_parse_list)==1:
                plot_list=plot_parse_list.find_all('p')
                for plt in plot_list:
                    storyLine=re.sub('</p>|<p>','',str(plt))
            else:
                plot_len_dic={}
                for plot in plot_parse_list:
                    if re.search('synopsis',str(plot),re.I|re.S|re.M):
                        plot_parse_list.remove(plot)
                for plotStory in plot_parse_list:
                    plt_story=plotStory.find_all('p')
                    for plt in plt_story:
                        final_plotString=re.sub('</p>|<p>','',str(plt))
                        plot_len_dic[final_plotString]=len(str(final_plotString))
                    #plot_len_dic[plotStory]=len(str(plotStory.find_all('p')))
                for plot_key, plot_StringLen in plot_len_dic.items():
                    if plot_StringLen==max(plot_len_dic.values()):
                        storyLine=plot_key
            return(storyLine)  
print(extractPlot.extractStoryPlot('tt0376080'))

        
        

