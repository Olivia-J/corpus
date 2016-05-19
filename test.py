#from corpus.models import Word
#import nltk.corpus.reader.bnc as b
#bnc=b.BNCCorpusReader(root='/Users/xiaoxuisaac/Documents/BNC/Texts/', fileids=r'[A-K]/\w*/\w*\.xml')
import nltk
from lib.text import *
from corpus.models import *
from nltk.stem.lancaster import LancasterStemmer



st=LancasterStemmer()
for word in Word.objects.filter(stem=None):
    word.stem=st.stem(word.word)
    print word.word, word.stem
    word.save()
print x

f=open("/source/passage/prince-excerpt1")
passage=f.read()
lemma_pr=lemma(pr)
prince=Text(pr,lemma_pr)
#print prince.vocab()['stay']
print len(prince.sentences)
print len(prince.lemma_sentences)

#print prince.example("stay")