
# coding: utf-8

# In[9]:

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import smtplib
import os


# In[12]:

#import the link and read it as a beautiful soup object
link="http://thehistoryofrome.typepad.com/revolutions_podcast/tours.html"
html=urlopen(link)
bsObj=BS(html,"html.parser")


# In[13]:

names=bsObj.find("div",{"class":"entry-body"}).findAll("p")


# In[5]:

list_text=[]
for name in names:
    list_text.append(name.get_text())
list_text


# In[6]:

list_text_original=['\xa0',
 'New History of Rome Tours are happening! Fall 2016!',
 'Italy',
 'or',
 'Spain',
 'Details and sign-ups coming soon.',
 '\xa0']


# In[7]:

list_text==list_text_original


# In[21]:

#writting the email
uname=os.environ.get("UNAME")
psw=os.environ.get("EMAIL_PASS")
address="@ymail.com"
to_mail=uname+address
from_mail=uname+address

msg="hey girl hit up this page for some mad deals: \n"+link
server = smtplib.SMTP('smtp.ymail.com:587')
server.starttls()
server.login(unam,psw)
server.sendmail(from_mail, to_mail,msg)
server.quit()


# In[27]:

x={"big mike":"the boys"}
x.get("big mike")

