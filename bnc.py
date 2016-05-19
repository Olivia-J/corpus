import nltk
from lib.text import *
from corpus.models import *
from nltk.stem.lancaster import LancasterStemmer
import codecs
import sys
from BeautifulSoup import BeautifulSoup as BS
import xml.etree.ElementTree as ET
import re
import fnmatch
import os
from lxml import etree


files=[]
for file in os.listdir("/Users/xiaoxuisaac/Documents/BNC/corpus/"):
    if fnmatch.fnmatch(file, '*.xml'):
        if len(Passage.objects.filter(identification="BNC-"+file))==0:
         files.append(file)
         
def add_xml(xml):
 #print xml
 file=read("/Users/xiaoxuisaac/Documents/BNC/corpus/"+xml).encode('utf-8')
 file=re.sub(r'<!-.*?-->','',file)
 #print file
 parser = etree.XMLParser(recover=True)
 raw=etree.fromstring(file, parser=parser)
 #raw=ET.fromstring(file) 
 try:
  title=ET.tostring(raw.find('.//bibl').find('.//title'),encoding='UTF-8')
 except:
     title=ET.tostring(raw.find('.//title'),encoding='UTF-8')
 title=re.sub(r'<.*?>','',title)
 try:
  author=''
  author=ET.tostring(raw.find('.//bibl').find('.//author'),encoding='UTF-8')
  author=re.sub(r'<.*?>','',author)
 except: pass
 try:
  p=ET.tostring(raw.find('.//wtext'),encoding='UTF-8')
 except:
  p=ET.tostring(raw.find('.//stext'),encoding='UTF-8')
 p=re.sub(r'<.*?>','',p)
 note=ET.tostring(raw.find('.//fileDesc'),encoding='UTF-8')
 note=re.sub(r'<.*?>','',note)
 lemma_p=lemma(p)
 p_db=Passage(
    content = p,
    lemma = lemma_p,
    book = title,
    author = author,
#    section = "excerpt1",
    note = note,
    identification = "BNC-"+xml
    )
 p_db.save()
 passage=Text(p,lemma_p)
 
 vocab=passage.vocabulary()
 i=1

 st=LancasterStemmer()

 newvocab=[]
 difficulty=0.0
 for v in vocab:
    if len(Word.objects.filter(word=v))==0:
#        print i,"," +v#+",",vocab[v], Word.objects.filter(stem=st.stem(v))
        i+=1
        w=Word(word=v)
        w.save()
    w=Word.objects.get(word=v)
    p_db.vocab.add(w)
 p_db.save()

 print xml ,i, len(vocab), len(vocab)/i

n=len(files)+1
for xml in files[:]:
    n=n-1
    print n
    try: 
        add_xml(xml)
    except:
        print xml+" corrupted"