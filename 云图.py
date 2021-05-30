# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:41:30 2021

@author: 35865
"""
from wordcloud import WordCloud
import matplotlib.pyplot as plt

filename = "C:/Users/35865/Desktop/问题3/自建特征值/type7_prop7_汇总.txt"

with open(filename,encoding='utf-8') as f:
 mytext = f.read()
 
wordcloud = WordCloud(font_path='C:/Windows/Fonts/simhei.ttf').generate(mytext)
 

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")