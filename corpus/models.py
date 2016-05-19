from django.db import models

# Create your models here.
class WordList(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
class Word(models.Model):
    word = models.CharField(max_length=30,primary_key=True)
    wordlist = models.ManyToManyField(WordList,blank=True, null=True)
    en_def = models.CharField(max_length=500)
    webster_def = models.CharField(max_length=500)
    cn_def = models.CharField(max_length=500)
    pospeech = models.CharField(max_length=100)
    stem =  models.CharField(max_length=30, blank=True, null=True)
    sentence = models.CharField(max_length = 800)
    webster_sentence = models.CharField(max_length = 800)
    difficulty = models.DecimalField(blank=True, null=True,max_digits=5, decimal_places=2)
    calc_diff = models.DecimalField(blank=True, null=True,max_digits=26, decimal_places=13)
    freq = models.IntegerField(blank=True, null=True)
    bncfreq = models.IntegerField(blank=True, null=True)
    ngramsfreq = models.DecimalField(blank=True, null=True,max_digits=15, decimal_places=13)
    origin = models.CharField(max_length=30)
    latin = models.CharField(max_length=100)
    vocabulary_short=models.CharField(max_length=800)
    vocabulary_long=models.CharField(max_length=1500)
    
    def __str__(self):
        return self.word
        
class PassageList(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
        
class Passage(models.Model):
    content = models.TextField()
    lemma = models.TextField()
    section = models.CharField(max_length=30)
    book = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    note = models.CharField(max_length=2000)
    identification =  models.CharField(max_length=100, unique=True)
    beyond_sat_rate = models.IntegerField(blank=True, null=True)
    sat_rate = models.IntegerField(blank=True, null=True)
    toefl_rate = models.IntegerField(blank=True, null=True)
    vocab_rate = models.IntegerField(blank=True, null=True)
    lexile = models.IntegerField(blank=True, null=True)
    passagelist = models.ManyToManyField(PassageList,blank=True, null=True)
    vocab = models.ManyToManyField(Word,blank=True, null=True)
    def __str__(self):
        return self.book

class BNCword(models.Model):
    word = models.CharField(max_length=30,primary_key=True)
    bncfreq = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.word
    