#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
import numpy as np


# In[2]:


#web_url="https://www.amazon.in/Bassheads-105-Wired-Headset-White/dp/B08YYRDCDV/ref=sr_1_5"
httpObj=urlopen('https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1')
first_page= httpObj.read()
print(first_page)


# In[3]:


first_page_soup= soup(first_page)


# In[4]:


pages_link = first_page_soup.findAll('a',{'class':'ge-49M'})
page_link = 'https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='
f=open('TELEVIS_info.csv','wb')
f.write('Product_Name,Stars,Ratings,Reviews,current_price,MRP,channel,Operating_system,Picture_qualtiy,Speaker,Frequency,Image_url\n'.encode())


for i in range(1,46):
    link = page_link + str(i)
    http =  urlopen(link)
    page_data = http.read()
    soupdata = soup(page_data)
    containers=soupdata.findAll('div',{'class':'_2kHMtA'})
    #start from here
    for container in containers:
        
    #find product name
        product = container.find('div',{'class':'_4rR01T'})    
        Product_Name= product.text.split()[0].strip()
    #print(Product_Name)
    
    #find product stars
        star =container.find('div',{'class':'_3LWZlK'})
        try:
            Stars= star.text 
       #print(star.text)
        except:
            Stars=0
        #print(star)
        
        #find product rating and reviews
        Rating = container.find('span',{'class':'_2_R_DZ'})
        try:
            ratRev=re.findall('\d+,*\d+,*\d+',Rating.text)
            Ratings=ratRev[0].replace(',','')
            Reviews=ratRev[1].replace(',','')
        
        
        except:
            Ratings=0
            Reviews=0
    #print("rate:",Ratings, "review:",Reviews)
    #find current price
        current_price = container.find('div',{'class':'_30jeq3 _1_WHN1'}).text.replace(',','')
    #print("current_price:",current_price.text)
    
    #find current MRP
        mrp = container.find('div',{'class':'_3I9_wc _27UcVY'})
        try:
            MRP = mrp.text.replace(',','')
        #print("MRP:",MRP.text)
        except:
            MRP=0
        #print("MRP:",0)

     #find infoabout product having same class name from list   
        info = container.findAll('li',{'class':'rgWa7D'})
        channel =info[0].text
        Operating_system =info[1].text
        Picture_qualtiy =info[2].text
        Speaker =info[3].text
        Frequency =info[4].text    
    #print(channel,Operating_system,Picture_qualtiy,Speaker,Frequency)
    
        Image= container.img
    #print(Image.get('src'))
        Image_url=Image.get('src')
    #print(Image_url)
    
    
        print(Product_Name,Stars,Ratings,Reviews,current_price,MRP,channel,Operating_system,Picture_qualtiy,Speaker,Frequency,Image_url)
    
        f.write(f"{Product_Name},{Stars},{Ratings},{Reviews},{current_price},{MRP},{channel},{Operating_system},{Picture_qualtiy},{Speaker},{Frequency},{Image_url}\n".encode())
        print('\n')

f.close()


# In[5]:


import pandas as pd
df= pd.read_csv('C:/Users/HP/beautiful_soap/TELEVISIONN_info.csv',error_bad_lines=False)
df.head()


# In[6]:


df.shape


# In[ ]:




