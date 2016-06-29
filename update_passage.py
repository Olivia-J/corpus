import nltk
from lib.text import *
from corpus.models import *
from nltk.stem.lancaster import LancasterStemmer
import codecs
import sys
from update_ngrams import update_ngram
from lib.webster import webster
import csv
import subprocess

def update_newvocab(newvocab):
    ngrams_vocab=[]
    for v in newvocab:
        try:
         word = Word.objects.get(word=v)
        except:
         word = Word(v)
         word.save()
        if word.webster_def=='' or word.sentence=='' or word.pospeech=='':
            print word.word, word.webster_def, word.sentence, word.pospeech
            print word.word=='', word.webster_def=='', word.sentence=='', word.pospeech==''
            web = webster(v.encode('utf-8'))
            word.webster_def=web[0]
            word.sentence=web[1]
            word.pospeech=web[2]
            word.save()
            print word.word, word.webster_def, word.sentence, word.pospeech
        if word.ngramsfreq==None:
            ngrams_vocab.append(v)
    
    print len(ngrams_vocab)
    update_ngram(ngrams_vocab)
    

def csv_out(vocab):
    f=open('source/passage_vocab/'+filename+'.csv','w')
    for word in vocab:
        w=Word.objects.get(word=word)
        if w.difficulty > 5 and w.webster_def!='N/A':
            f.write(w.word.encode('utf-8')+','+str(w.difficulty)+',')
            f.write(w.pospeech.encode('utf-8')+',"'+w.webster_def.encode('utf-8')+'",'+'"'+w.sentence.encode('utf-8')+'"\n')
    f.close()

def select(vocab):
    selected=[]
    for v in vocab:
        w=Word.objects.get(word=v)
        if w.difficulty > 5 and w.webster_def!='N/A':
            selected.append(w)
            return selected

def latex_out():
    f=open('source/passage_vocab/'+filename+'.tex','w')
    parts={'noun':'n.','verb':'v.','adjective':'adj.','adverb':'adv.', 'interjection':'interj.','geographical name':'geo.'}
    csvfile = open('source/passage_vocab/'+filename+'.csv', 'rU')
    header=\
'\\documentclass[a4paper]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{longtable}\n\
\\usepackage[margin=1in]{geometry}\n\
\n\
\\title{Vocabulary in \\textit{Illiad}}\n\
\\author{Compiled by AcadeMe for the Homer Project}\n\
\\date{May 2016}\n\
\n\
\\usepackage{natbib}\n\
\\usepackage{graphicx}\n\
\n\
\\begin{document}\n\
\n\
\\maketitle\n\
\\begin{longtable}{llp{11cm}}\n'
    footer=\
'\end{longtable}\n\
\end{document}\n'
    vocab = csv.reader(csvfile, delimiter=',', quotechar='"', dialect=csv.excel_tab)
    formula = '\\textbf{[WORD]} & [POSPEECH] &  [Definition]\\\\\n & & \\textit{[SENTENCE]}\\\\[0.08cm]\n'
    formula_no_sen = '\\textbf{[WORD]} & [POSPEECH] &  [Definition]\\\\[0.08cm]\n'
    f.write(header)    
    for row in vocab:
        if row[4]=='N/A':
            entry=formula_no_sen
        else:
            entry=formula.replace('[SENTENCE]',row[4])
        entry=entry.replace('[WORD]',row[0]).replace('[Definition]', row[3])
        try:
            part=parts[row[2]]
        except:
            part=row[2]
        entry=entry.replace('[POSPEECH]',part)
        f.write(entry)
    f.write(footer)
    f.close()
     
def pdf_out():
 latex_out()
 subprocess.call(['pdflatex','-output-directory=source/passage_vocab/','source/passage_vocab/'+filename+'.tex'],shell=False)


if True:
# f=codecs.open("source/passage/og-list.txt",encoding='utf8')
# p=f.read()
 filename='illiad_pickus'
 p=read("source/passage/"+filename+".txt")
 #print sdhbi
# p=p.decode('utf-8')
 lemma_p=lemma(p)
 p_db=Passage(
    content = p,
    lemma = lemma_p,
    book = "The Prince",
    section = "excerpt1",
    note = "Hongyang@HSBF Oct 2015\n",
    identification = "prince-excerpt1"
    )
else:
    p_db=Passage.objects.filter(book__contains__="Prince")[0]
    p=p_db.content
    lemma_p=p_db.lemma

def initial(p):
    passage=Text(p,lemma_p)
    vocab=passage.vocabulary()
    i=1
    st=LancasterStemmer()
    newvocab=[]
    difficulty=0.0

    #for v in vocab:
    #    if len(Word.objects.filter(word=v))==0:
    #        print i,"," +v#+",",vocab[v], Word.objects.filter(stem=st.stem(v))
    #        i+=1
    #        newvocab.append(v)
    #    else:
    #        diffi=float(Word.objects.get(word=v).difficulty)
    #        if diffi >10:
    #            print v, diffi 
    #        difficulty+=vocab[v]*float(Word.objects.get(word=v).calc_diff)

    difficulty=difficulty/len(passage.tokens)
    print len(vocab)
    #p_db.save()
    return vocab, newvocab
