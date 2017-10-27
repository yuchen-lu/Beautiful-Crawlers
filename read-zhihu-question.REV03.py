# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:15:06 2017

@author: yuchen
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import numpy as np
import ssl
import re
import os
question = str()
Qtitle=list()
url=str()
pagenum=1 
while(True):
    PageNumAdded=0
    questionpage='https://www.zhihu.com/people/gao-xiang-24-90/following/questions?page='
    
    
       
    url=questionpage+str(pagenum)
      
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    html=urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html)
    
    
    ##tags = soup('title')
    #for tag in tags:
    #    print(tag)
    #links = re.findall('a href="/question/"' , html)
    
    #for link in links:
     #   print(link.decode())
    
    #print(soup.prettify())
    letters1 = soup.find_all("div", class_="QuestionItem-title")
    #print(type(letters))
    #print(letters[3])
    
    
    
    for letter in letters1:
    #    Qtitle[letter.a.get_text()]["Qnumber"] = letter.a["href"]
    #    print(letter.get_text())
        Qtitle.append(letter.get_text())  #get text between<> and <>
    
    
    #print(Qtitle)    
        
    #letters2 = soup.find_all("div", data-config="{"apiAddress":"/api/v4/","deployEnv":"production"}")
    # extract a whole set of div with data-config:.......
    letters2 = soup.find("div", {'data-config':'{"apiAddress":"/api/v4/","deployEnv":"production"}'}).attrs['data-state']
    
    
                 
    
    newlist = list()
    newlist = letters2.split(',')
    #print(newlist)
    starts = [n for n, l in enumerate(newlist) if l.startswith('"title"')]
    #print(starts)
    newerlist =list()
    
    for yo in starts:
       newerlist.append(newlist[yo])
    
    for haha in newerlist:
        final1 = haha.split(":")
       # final2 = final1.replace('"','')
        oddeven = 1   
        for yoyo in final1:
            final2 = yoyo.replace('"','')
            #print(final2)
            
            if (oddeven//2) != 0:
                Qtitle.append(final2)
                PageNumAdded=PageNumAdded+1
            oddeven = oddeven + 1 
      
    if (PageNumAdded==0):
        print('thats it, total',pagenum,'pages of questions,',len(Qtitle)+1, 'titles stored')       
        break
    pagenum=pagenum+1
    
titlefile=open('Question-title.txt','w')    
for title in Qtitle:
    titlefile.write(title)
    
titlefile.close()

#os.startfile(titlefile)
