# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

import ssl
import re
url='https://www.zhihu.com/people/gao-xiang-24-90/following/questions'



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

Qtitle=list()

for letter in letters1:
#    Qtitle[letter.a.get_text()]["Qnumber"] = letter.a["href"]
#    print(letter.get_text())
    Qtitle.append(letter.get_text())  #get text between<> and <>


#print(Qtitle)    
    
#letters2 = soup.find_all("div", data-config="{"apiAddress":"/api/v4/","deployEnv":"production"}")
# extract a whole set of div with data-config:.......
letters2 = soup.find("div", {'data-config':'{"apiAddress":"/api/v4/","deployEnv":"production"}'}).attrs['data-state']
#print(letters2)#, data-config_='{"apiAddress":"/api/v4/","deployEnv":"production"}')
#print(letters2)
#print(type(letters2)) #return stings
#print (letters2)
#mydict = dict()
#mydict = (e.split('"title":') for e in letters2 #.split(','))
#print(mydict)

             
#for element in letters2:
    #print (element)
#print(letters2)

#element=list()
#for element in letters2:
#    print(element)
 #   highest-data =  element.find_all("div", {'data-reactid':'20'}).attrs['data-state']   
#data-state is a string


newlist = list()
newlist = letters2.split(',')
#print(newlist)
starts = [n for n, l in enumerate(newlist) if l.startswith('"title"')]
#print(starts)
newerlist =list()

for yo in starts:
   newerlist.append(newlist[yo])
#print(newlist[starts])
#for yo in newlist:
    #print(yo.startswith('title')) only print true/false
 #   print(yo
#print(newerlist) 
#str1=' '.join(newerlist)
#nonsense = str1.find("title")
for haha in newerlist:
    final1 = haha.split(":")
   # final2 = final1.replace('"','')
    oddeven = 1   
    for yoyo in final1:
        final2 = yoyo.replace('"','')
        print(final2)
        
        if (oddeven//2) != 0:
            Qtitle.append(final2)
        oddeven = oddeven + 1    
            
      #  Qtitle.append(yoyo)
    
    #Qtitle.append(final1[1])    
#print(str1)
#print(str1)
#newerlist3 = newerlist.split('？"',')
#print(newerlist3)
#indexi=0
#location = list()

#if (indexi<len(str1)):
 #   if( str1[indexi] == 'title'):
  #    location.append(indexi)
  #  indexi=indexi+1    
    
    
#print(location)