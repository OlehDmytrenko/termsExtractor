# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2:44:23 2022
Edited on Wed Fri 25 11:12:34 2022
Edited on Wed Sat 26 23:57:53 2022
Edited on Sun Mar 06 04:44:17 2022

@author: Олег Дмитренко

"""
import os, subprocess
subprocess.run('python -m venv '+os.getcwd(), shell=True)
from modules import packagesInstaller
packages = ['fasttext', 'textblob']
packagesInstaller.setup_packeges(packages)

import fasttext, textblob
from textblob import TextBlob as tb
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from modules import defaultLoader

def built_words(sent, Words, nlpModel, stopWords):
    WordsTags = []
    words = word_tokenize(sent)
    for word in words:
        i = nlpModel.normal_forms(word)[0]
        j = str((nlpModel.parse(word)[0]).tag.POS)
        if j=='NPRO':
            j = 'NOUN'
        WordsTags.append((i,j))
        if (i not in stopWords) and (j == 'NOUN'): 
            Words.append(i)
    return WordsTags, Words

def built_bigrams(WordsTags, Bigrams, stopWords):
    for i in range(1, len(WordsTags)):
        w1 = WordsTags[i-1][0] 
        w2 = WordsTags[i][0]
        t1 = WordsTags[i-1][1]
        t2 = WordsTags[i][1]
        if (t1 == 'ADJF') and (t2 == 'NOUN') and (w1 not in stopWords) and (w2 not in stopWords):
            Bigrams.append(w1+'_'+w2)
    return Bigrams

def built_threegrams(WordsTags, Threegrams, stopWords):
    for i in range(2, len(WordsTags)):
        w1 = WordsTags[i-2][0]
        w2 = WordsTags[i-1][0]
        w3 = WordsTags[i][0]
        t1 = WordsTags[i-2][1]
        t2 = WordsTags[i-1][1]
        t3 = WordsTags[i][1]
        if (t1 == 'NOUN') and ((t2 == 'CCONJ') or (t2 == 'PREP')) and (t3 == 'NOUN') and (w1 not in stopWords) and (w3 not in stopWords):
            Threegrams.append(w1+'_'+w2+'_'+w3)
        elif (t1 == 'ADJF') and (t2 == 'ADJF') and (t3 == 'NOUN') and (w1 not in stopWords) and (w2 not in stopWords) and (w3 not in stopWords):
            Threegrams.append(w1+'_'+w2+'_'+w3)
    return Threegrams

def nl_processing(text, nlpModel, stopWords):
    Words = []
    Bigrams = []
    Threegrams = []
    sents = sent_tokenize(text)
    for sent in sents:
        WordsTags, Words = built_words(sent, Words, nlpModel, stopWords)
        if len(WordsTags)>2:
            Bigrams = built_bigrams(WordsTags, Bigrams, stopWords)
        if len(WordsTags)>3:
            Threegrams = built_threegrams(WordsTags, Threegrams, stopWords)
    return Words, Bigrams, Threegrams

def lang_detect(message, defaultLangs, nlpModels, stopWords):
    lidModel = fasttext.load_model('lid.176.ftz')
    if message.isspace():
        return 'kv'
    else:
        try:
            # get first item of the prediction tuple, then split by "__label__" and return only language code
            lang = lidModel.predict(message)[0][0].split("__label__")[1]
        except:
            return "en"
    if lang not in defaultLangs:
        lang = defaultLoader.download_model(defaultLangs, nlpModels, lang)
        defaultLoader.load_stop_words(defaultLangs, stopWords, lang)
    return lang
