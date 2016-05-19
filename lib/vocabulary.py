import urllib2
from BeautifulSoup import BeautifulSoup as BS
import re

def vocabulary(word):
 response = urllib2.urlopen('https://www.vocabulary.com/dictionary/'+word)
 html=BS(response.read())
 short = 'N/A'
 full = 'N/A'
 try:
     raw=html.findAll('p',{"class":"short"})[0]
     short=re.sub(r'<.*?>','',raw.renderContents())
 except:
     pass
 try:
     raw=html.findAll('p',{"class":"long"})[0]
     full=re.sub(r'<.*?>','',raw.renderContents())
 except:
     pass
 return short, full