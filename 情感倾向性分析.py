# -*- coding: utf-8 -*-
"""
Created on Fri May 28 19:02:38 2021

@author: 35865
"""
import xlrd
from aip import AipNlp
import numpy as np
import pandas as pd
from pandas import DataFrame
import time

""" 你的 APPID AK SK """

APP_ID = '	24245258'
API_KEY = '8xjWxdMjtVNsr4WigDzwWmnh'
SECRET_KEY = '4qIiKSRuvZ7DWmVk6pA7lppWCQlkNe5V'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
#########################################################

# import sys
# print(sys.path) 查看当前文件说在目录
# 打开文件
workbook=xlrd.open_workbook(r'C:/Users/35865/Desktop/文本分析TAG分类/评论合并/评论合并.xlsx')

# 获取sheet名称
sheet_name = workbook.sheet_names()[0] #sheet索引从0开始
# print(sheet_name)

 # 根据sheet索引或者名称获取sheet内容
sheet = workbook.sheet_by_index(0) # sheet索引从0开始
# print(sheet)

for i in range(1246):
# 4、获取指定单元格里面的值
   i=sheet.cell_value(i,0)#sheet.cell_value(第几行,第几列)
   data = i.replace(u'\xa0', u' ') .replace(u'\xb3', u' ') .replace(u"\xaf",u" ").replace('\uf06a', u' ').replace(u'\u02dc', u' ')
   
   result=client.sentimentClassify(data)
   
   pf = pd.DataFrame(result,index=[0])
   
   print(pf)
   
   pf.to_csv('C:/Users/35865/Desktop/文本分析TAG分类/评论合并/评论合并返回结果_第三次跑_range_1246.csv',encoding = 'utf_8_sig',mode='a', header=False) #绝对位置
   
   time.sleep(1)
   
################################################################