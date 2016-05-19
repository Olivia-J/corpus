from nltk.stem.wordnet import WordNetLemmatizer 
import nltk
class Lemmatizer(object):    
    def lemmatize(self,word):
        names=nltk.corpus.names.words("male.txt")+nltk.corpus.names.words("female.txt")
        if word[0].isupper() and word in names:
                return word        
        try:
            y=word.lower()
            y=WordNetLemmatizer().lemmatize(y, pos='v')
            y=WordNetLemmatizer().lemmatize(y, pos='a')
            y=WordNetLemmatizer().lemmatize(y, pos='r')
            if len(y)>2:
             y=WordNetLemmatizer().lemmatize(y, pos='n')
            return y
        except:
            return word.decode('utf-8')
    def lemmatize_passage(self,passage):
        tokens = nltk.word_tokenize(passage)
        lemma_passage=''
        for word in tokens:
            lemma=lemmatize(word)
            if word[0].isalpha() or word[0].isdigit():
                lemma_passage=lemma_passage+' '+lemma
            else:
                lemma_passage=lemma_passage+lemma
        return lemma_passage