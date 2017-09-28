
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


titles=list()

url='https://www.zhihu.com/people/funkycastor/following/questions'

soup = BeautifulSoup(sdata)



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html=urllib.request.urlopen(url,context=ctx).read()
#print(html)
yolo= BeautifulSoup(html,'html.parser')

tag =soup.findall()
tags1 = yolo('span')
tags2 = yolo('div')

for tag in tags1:
        titles.append(tag.contents[0])
        




print(titles)
        

