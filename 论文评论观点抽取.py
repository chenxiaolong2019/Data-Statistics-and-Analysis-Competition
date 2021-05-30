# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:44:03 2021

@author: 35865
"""
import xlrd
from aip import AipNlp
import numpy as np
import pandas as pd
from pandas import DataFrame
import time

""" 你的 APPID AK SK """

APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

############################################################


workbook=xlrd.open_workbook(r'C:/Users/35865/Desktop/文本分析TAG分类/评论合并/评论合并.xlsx')
sheet_name = workbook.sheet_names()[0] #sheet索引从0开始
sheet = workbook.sheet_by_index(0) # sheet索引从0开始

for i in range(1246):
# 4、获取指定单元格里面的值
   i=sheet.cell_value(i,0)#sheet.cell_value(第几行,第几列)
   data = i.replace(u'\xa0', u' ') .replace(u'\xb3', u' ') .replace(u"\xaf",u" ").replace('\uf06a', u' ').replace(u'\u02dc', u' ')

   text = data
#百度模型
   client.commentTag(text);
   options = {}
   options["type"] = 7
   result=client.commentTag(text, options)
#end
#写入文件   
   pf = pd.DataFrame.from_dict(result,orient='index').T
   
   print(pf)
   
   pf.to_csv('C:/Users/35865/Desktop/评论观点抽取/第一次debug后/评论观点抽取第4次跑_sleep1_type7_range1246.csv',encoding = 'utf_8_sig',mode='a', header=False) #绝对位置
   time.sleep(1)
   
