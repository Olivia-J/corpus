import nltk.corpus.reader.bnc as reader
import random

class Example(object):
    def example(self, word, num):
        
    def _bnc_generate():
        firstlist=['A','B','C','D','E','F','G','H','I','J']
        indexlist=['1','2','3','4','5','6','7','8','9','0',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D',
        'F','G','H','J','K','L','Z','X','C','V','B','N','M']
        flag = True
        for flag:            
            field = r'/'+random.choice(firstlist)+random.choice(indexlist)+random.choice(indexlist)
            try:
                bnc=reader.BNCCorpusReader(root='/Users/xiaoxuisaac/Documents/BNC/Texts/', fileids=field[0]+"/"+field[:2]+"/"+field[:3]+.xml')
                flag = False
            except:
                pass
        return bnc