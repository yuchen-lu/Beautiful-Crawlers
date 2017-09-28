# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:08:45 2017

@author: Yuchen
"""

"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


titles=list()

url='https://www.zhihu.com/people/funkycastor/following/questions'




# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html=urllib.request.urlopen(url,context=ctx).read()
#print(html)
soup= BeautifulSoup(html,'html.parser')
tags = soup('span')
#print(tags)
yo1=soup("span",{"class":"QuestionItem-title"})
print(yo1)
yo2=soup("div",{"class":"QuestionItem-title"})
print(yo2)

#print(soup)
#tags1= soup.findall('span',{'class':"QuestionItem-title"})
#tags2 = soup.find_all('div',{'class':"QuestionItem-title"})

#print(tags1)




