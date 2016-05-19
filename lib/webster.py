import urllib2
import xml.etree.ElementTree as ET

def sample(child):
    childstr=ET.tostring(child)
    childstr=childstr.replace('<it>','').replace('</it>','')    
    childstr=childstr.replace('<phrase>','').replace('</phrase>','')   
    child= ET.fromstring(childstr)
    try:
        return child.find('.//vi').text
    except:
        return 'N/A'

def definition(child):
    childstr=ET.tostring(child)   
    childstr=childstr.replace('<d_link>','').replace('</d_link>','')
    childstr=childstr.replace('<sx>','').replace('</sx>','')
    childstr=childstr.replace('<phrase>','').replace('</phrase>','')
    childstr=childstr.replace('<it>','').replace('</it>','')    
    childstr=childstr.replace('<un>','').replace('</un>','')
    childstr=childstr.replace('<fraction>','').replace('</fraction>','')
    childstr=childstr.replace('<inf>','').replace('</inf>','')
    
    child= ET.fromstring(childstr)
    try:
        return child.text[1:]
    except:
        return 'N/A'


def webster(word):
 try:
  response = urllib2.urlopen('http://www.dictionaryapi.com/api/v1/references/learners/xml/'
    +word+'?key=40d96316-f219-4661-893b-62df83769d28')
  root= ET.fromstring(response.read())
  d='N/A'
  s='N/A'
  pospeech='N/A'
  #define the derevatives as its orginal word
  #if word not in root[0].attrib['id']:
  #    word=root[0].attrib['id'].replace('[1]','')
  for child in root:
#     print "child in root", child.attrib['id']
     if word.lower() in child.attrib['id'].lower() and ' ' not in child.attrib['id'] and '-' not in child.attrib['id']:
      if child.find(".//fl").text=='verb':
         return definition(child.find(".//dt")), sample(child.find(".//def")), 'verb'
      elif child.find(".//fl").text=='adjective':
#         print "here",child.find(".//dt").text
         return definition(child.find(".//dt")), sample(child.find(".//def")), 'adjective'
      elif child.find(".//fl").text!='noun':
         return definition(child.find(".//dt")), sample(child.find(".//def")), child.find(".//fl").text
      elif d=='N/A':
#         print "here",child.find(".//dt").text 
         d=definition(child.find(".//dt"))
         s=sample(child.find(".//def"))
         pospeech = child.find(".//fl").text
  return d,s, pospeech
 except:
  response = urllib2.urlopen('http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'
     +word+'?key=11f82c71-15d3-4d60-ba76-6c2a62b57a0a')
  root= ET.fromstring(response.read())
 #define the derevatives as its orginal word 
 # if word not in root[0].attrib['id']:
 #     word=root[0].attrib['id'].replace('[1]','')
  d='N/A'
  s='N/A'
  try:
   for child in root:
     if word.lower() in child.attrib['id'].lower() and ' ' not in child.attrib['id'] and '-' not in child.attrib['id']:
       if child.find(".//fl").text=='verb':
          return definition(child.find(".//dt")), sample(child.find(".//def")), 'verb'
       elif child.find(".//fl").text=='adjactive':
          return definition(child.find(".//dt")), sample(child.find(".//def")), 'adjective'
       elif child.find(".//fl").text!='noun':
          return definition(child.find(".//dt")), sample(child.find(".//def")), child.find(".//fl").text
       elif d=='N/A':
          d=definition(child.find(".//dt"))
          s=sample(child.find(".//def"))
          pospeech = child.find(".//fl").text
   return d,s,pospeech
  except:
   return 'N/A','N/A','N/A'