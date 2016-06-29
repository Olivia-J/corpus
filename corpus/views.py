from .forms import *
from django.views.generic.edit import FormView

# from django.views.generic.base import TemplateView

from django.http import HttpResponse
from django.views.generic import View

from django.corpus.models import *

from django.http import HttpResponseRedirect
from django.shortcuts import render

def ArticleView(request):
    if request.method == 'POST':
        article=ArticleForm(request.POST)
        if article.is_valid()
        generate_WordList(article.cleaned_data)
        
        return HttpResponseRedirect('/WordList/')
    else:
        article = ArticleForm()
        return render(request, '', {'article':article})

def WordListView(request, selected):
    if request.method == 'POST':
        v=[]
        for w in selected:
            v.append(WordForm('word'=w))
    for i in v:
        if i.is_valid():
            generate_WordBank(i)
        
        return HttpResponseRedirect('/WordBank/')
    else:
        return HttpResponseRedirect('/Article/')

class WordBankView(TemplateView):
    template_name = "WordBank.html"
    
    def get_context_data(self. **kwargs):
        context=super(WordBankView,self).get_context_data(**kwargs)
        context['wordbank']=wordbank

def generate_WordList(article):
    initial(article)
    update_newvocab(newvocab)
    select(vocab)
    req.session['selected'] = selected
        
def generate_WordBank(i):
    wordbank=[]
    # i is an instance of WordForm which represents a word and its CheckBox Result
    if i.cleaned_data=True:
        wordbank.append(Word.objects.get(word=i.word))
        return wordbank
    req.session['wordbank']=wordbank
    del req.session['selected']
