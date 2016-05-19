import codecs
import sys
import subprocess
import csv
import random

filename='rights_man_q'

def quiz_pdf_out():
 subprocess.call(['pdflatex','-output-directory=source/passage_vocab/','source/passage_vocab/'+filename+'_quiz.tex'],shell=False)
 subprocess.call(['pdflatex','-output-directory=source/passage_vocab/','source/passage_vocab/'+filename+'_answer.tex'],shell=False)
 

csvfile = open('source/passage_vocab/'+filename+'.csv', 'rU')
vocab = csv.reader(csvfile, delimiter=',', quotechar='"', dialect=csv.excel_tab)
t=1
i=0
Word=[]
Defin=[]
list=[]
set=[]
Answer=[]

for row in vocab:
    if i<5:
       if row[2] != '':
          word=row[0]
          D=row[3]
          Defin.append(D)
          Word.append(word)
          i=0
          t=t+1
       else:
	      i=i+1
    else:
	   break   

m=0
i=1
list.append([])
set.append([])
Answer.append([])
while i < t:
    if i<=((m+1)*10):
       l=Word[i-1]
       list[m].append(l)
       s=Defin[i-1]
       set[m].append(s)
       Answer[m].append(s)
       i=i+1	   
    else:
       m=m+1
       list.append([])
       set.append([])
       Answer.append([])

i=0
for i in range(m+1):
    random.shuffle(set[i])

ABC=['a','b','c','d','e','f','g','h','i','j']
CBA=['a','b','c','d','e','f','g','h','i','j']

f=open('source/passage_vocab/'+filename+'_quiz.tex','w')
header=\
'\\documentclass[a4paper]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{longtable}\n\
\\usepackage[margin=1in]{geometry}\n\
\n\
\\title{Vocabulary in \\textit{Rights of Man} Quiz}\n\
\\author{Compiled by AcadeMe for the Homer Project}\n\
\\date{April 2016}\n\
\\usepackage{chngpage}\n\
\\usepackage{array}\n\
\\usepackage{natbib}\n\
\\usepackage{graphicx}\n\
\n\
\\begin{document}\n\
\n\
\\maketitle\n\
\\begin{center}\n\
\\begin{tabular}{|c|c|c|c|m{.7\\textwidth}|}\n\
\\hline\n\
No. & Words & Answer & No. & Definition \\\\\n'
footer=\
'\end{tabular}\n\
\end{center}\n\
\end{document}\n'
middle=\
'\\hline\n\
\\end{tabular}\n\
\\end{center}\n\
\\begin{center}\n\
\\begin{tabular}{|c|c|c|c|m{.7\\textwidth}|}\n\
\\hline\n\
No. & Words & Answer & No. & Definition \\\\\n'
formula = '\\hline\n [NUMBER] & [WORD] & & [alphabet] &  [Definition]\\\\\n'
formula_no_sen = '\\hline\n & & & & \\\\\n'
f.write(header)
m=0
i=0
p=1
n=0
while p < t:
    if i<10:	   
       entry=formula.replace('[WORD]',list[m][i]).replace('[NUMBER]', str(p)).replace('[Definition]',set[m][i]).replace('[alphabet]',ABC[i])
       f.write(entry)
       i=i+1
       p=p+1	   
    else:
       m=m+1
       i=0	 
       if m<(4*n+3):
           f.write(formula_no_sen)
       else:
           f.write(middle)
           n=n+1		   
if i != 10:
   f.write('\\hline\n')   
f.write(footer)
f.close()	

f=open('source/passage_vocab/'+filename+'_answer.tex','w')
header=\
'\\documentclass[a4paper]{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{longtable}\n\
\\usepackage[margin=1in]{geometry}\n\
\n\
\\title{Vocabulary in \\textit{The Prince} Quiz Answer}\n\
\\author{Compiled by AcadeMe for the Homer Project}\n\
\\date{April 2016}\n\
\\usepackage{chngpage}\n\
\\usepackage{array}\n\
\\usepackage{natbib}\n\
\\usepackage{graphicx}\n\
\n\
\\begin{document}\n\
\n\
\\maketitle\n\
\\begin{center}\n\
\\begin{tabular}{|c|c|c|c|m{.7\\textwidth}|}\n\
\\hline\n\
No. & Words & Answer & No. & Definition \\\\\n'
footer=\
'\end{tabular}\n\
\end{center}\n\
\end{document}\n'
middle=\
'\\hline\n\
\\end{tabular}\n\
\\end{center}\n\
\\begin{center}\n\
\\begin{tabular}{|c|c|c|c|m{.7\\textwidth}|}\n\
\\hline\n\
No. & Words & Answer & No. & Definition \\\\\n'
formula_answer = '\\hline\n [NUMBER]  & [WORD] & [ANSWER] & [alphabet] &  [Definition]\\\\\n'
formula_no_sen = '\\hline\n & & & & \\\\\n'
f.write(header)
m=0
i=0
p=1
n=0
q=0
while p < t:
    if i<10:
       while Answer[m][i] != set[m][q]:
	         q=q+1
       CBA[i]=ABC[q]
       entry=formula_answer.replace('[NUMBER]',str(p)).replace('[WORD]',list[m][i]).replace('[ANSWER]',CBA[i]).replace('[Definition]',set[m][i]).replace('[alphabet]',ABC[i])
       f.write(entry)
       i=i+1
       p=p+1
       q=0	   
    else:
       m=m+1
       i=0	 
       if m<(4*n+3):
           f.write(formula_no_sen)
       else:
           f.write(middle)
           n=n+1		   
if i != 10:
   f.write('\\hline\n')   
f.write(footer)
f.close()

csvfile.close()
