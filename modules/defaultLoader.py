# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11:45:30 2022
Edited on Fri Feb 25 10:16:56 2022
Edited on Sat Feb 26 23:46:57 2022
Edited on Sun Mar 06 03:55:34 2022

@author: Олег Дмитренко

"""
import os, subprocess
subprocess.run('python -m venv '+os.getcwd(), shell=True)
from modules import packagesInstaller
packages = ['os', 'io', 'subprocess', 'pymorphy2', 'nltk', 'stop_words']
packagesInstaller.setup_packeges(packages)

import os
import io
import subprocess
from pymorphy2 import MorphAnalyzer
import nltk
from nltk.corpus import stopwords
from stop_words import safe_get_stop_words

def append_lang(lang, defaultLangs):
    try:
        defaultLangs.append(lang)
        with io.open("defaultLangs.csv", "a", encoding="utf-8") as file:
            file.write(lang+'\n')
            file.close()
    except:
        print ('Unexpected Error while adding new languade to default list!')
    return

def load_stop_words(defaultLangs, stopWords, lang):
    if os.path.isfile(lang+'.txt'):
        localStopWords = (io.open(lang+'.txt', 'r', encoding="utf-8").read()).split()
    else:
        localStopWords = []
    try:
        stopWords[lang] = set(safe_get_stop_words(lang) + localStopWords)
        #print (str(lang) + ' stop words was loaded successfully!')
    except:
        return "Error! Stop words can not be loaded!"      
    return stopWords

def load_default_stop_words(defaultLangs):
    try:
        nltk.download('stopwords')
    except:
        return "Error! NLKT stop words can not be loaded!"
    stopWords = dict()
    #checking if list is empty
    if defaultLangs:
        for lang in defaultLangs:
            if os.path.isfile(lang+'.txt'):
                localStopWords = (io.open(lang+'.txt', 'r', encoding="utf-8").read()).split()
            else:
                localStopWords = []
            try:
                stopWords[lang] = set(safe_get_stop_words(lang) + localStopWords)
                #print (str(lang) + ' stop words was loaded successfully!')
            except:
                return "Error! Stop words can not be loaded!"
    else:
        print('The <defaultLangs> list is empty!')
        print ('Please, enter below at least one language ! For example, "en" or any other availible at https://fasttext.cc/docs/en/language-identification.html')
        lang = input()
        append_lang(lang)
        stopWords = load_stop_words(defaultLangs, stopWords)
    return stopWords

def download_model(defaultLangs, nlpModels, lang):
    try:
        subprocess.run('pip install -U pymorphy2-dicts-'+lang, shell=True)
        append_lang(lang, defaultLangs) 
        print (str(lang) + ' pymorphy2 model was downloaded successfully!')     
    except:
        return 'ru'
    try:
        nlpModels[lang] = MorphAnalyzer(lang = lang)
        print (str(lang) + ' pymorphy2 model was loaded successfully!')
    except:
        return None      
    return lang

def load_default_models(defaultLangs):
    nlpModels = dict()
    #checking if list is empty
    if defaultLangs:
        for lang in defaultLangs:
            if lang not in nlpModels.keys():
                try:
                    subprocess.run('pip install -U pymorphy2-dicts-'+lang, shell=True)
                    print (str(lang) + ' pymorphy2 model was downloaded successfully!')   
                except:
                    return "Error! "+str(lang)+" language model can not be dowloaded!" 
            try:
                nlpModels[lang] = MorphAnalyzer(lang = lang)
                print (str(lang) + ' pymorphy2 model was loaded successfully!')
            except:
                return "Error! "+str(lang)+" language model is can not be loaded!"           
    else:
        print('The <defaultLangs> list is empty!')
        print ('Please, enter below at least one language ! For example, "en" or any other availible at https://fasttext.cc/docs/en/language-identification.html')
        lang = input()
        append_lang(lang, defaultLangs)
        nlpModels = download_model(defaultLangs, nlpModels)
    return nlpModels

def load_except_languages():
    try:
        exceptedLangs = (io.open("exceptedLangs.csv", 'r', encoding="utf-8").read()).split()
    except:
        exceptedLangs = ['en', 'he', 'zh', 'de', 'kv', 'tl', 'bcl', 'xal', 'ba', 'ga']
    return exceptedLangs

def load_default_languages():
    try:
        defaultLangs = (io.open("defaultLangs.csv", 'r', encoding="utf-8").read()).split()
    except:
        defaultLangs = ['uk', 'ru']
    return defaultLangs
