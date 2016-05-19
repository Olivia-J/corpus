from corpus.models import Word, WordList
import csv
from lib.lemmatizer import Lemmatizer

vocabfile=open("source/wordlist/barron")
temp=csv.reader(vocabfile)
vocab=[]
for w in temp:
    y=Lemmatizer().lemmatize(w[0])
    vocab.append(y)

wlname="barron"
try:
    wordlist=WordList.objects.get(name=wlname)
except:
    wordlist=WordList(name="barron")
    wordlist.save()
for w in vocab:
    try:
     entry=Word.objects.get(word=w)
    except:
     entry=Word(word=w)
     entry.save()
    
    entry.wordlist.add(wordlist)
    entry.save()