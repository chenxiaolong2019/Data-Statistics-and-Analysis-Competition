# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:07:56 2021

@author: 35865
"""
""" 你的 APPID AK SK """
from aip import AipNlp

APP_ID = '	2424'
API_KEY = '8xjWxdMjtVNsr4WiWmnh'
SECRET_KEY = '4qIiKSRuvZ7DWmVpWCQlkNe5V'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


################################################
#评论观点抽取
filename = "C:/Users/35865/Desktop/葛/优秀论文1.2.txt"
with open(filename,encoding='utf-8') as f:
 mytext = f.read()

mytext_1 = mytext.replace(u'\xa0', u' ') .replace(u'\xb3', u' ') .replace(u"\xaf",u" ").replace('\uf06a', u' ').replace(u'\u02dc', u' ') 


mytext_1
""" 调用评论观点抽取 """
client.commentTag(mytext_1);

""" 如果有可选参数 """
options = {}
options["type"] = 7

""" 带参数调用评论观点抽取 """
print(client.commentTag(mytext_1, options))


########################################################

