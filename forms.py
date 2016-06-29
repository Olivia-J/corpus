from django import forms
from corpus-master import update_passage
from corpus.models import *
from django.forms import ModelForm

class ArticleForm(forms.Form):
    article=forms.CharField()

class WordForm(forms.Form):
    word = models.CharField(max_length=30,primary_key=True)
    check = models.BooleanField(label=word, default=True)
