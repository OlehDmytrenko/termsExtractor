# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11:45:30 2022
Edited on Fri Feb 25 10:16:56 2022
Edited on Sat Feb 26 23:46:57 2022
Edited on Sun Mar  6 03:55:34 2022
Edited on Mon Mar  7 04:33:47 2022
Edited on Thu Mar  8 05:55:54 2022
Edited on Wed Mar  9 07:39:23 2022

@author: Олег Дмитренко

"""
from __modules__ import packagesInstaller, textProcessor
packages = ['os', 'io', 'stop_words']
packagesInstaller.setup_packeges(packages)

import os, io
from stop_words import safe_get_stop_words

def load_stop_words(defaultLangs, defaultSWs, lang):
    if os.path.isfile(lang+'.txt'):
        localStopWords = (io.open(lang+'.txt', 'r', encoding="utf-8").read()).split()
    else:
        localStopWords = []
    try:
        defaultSWs[lang] = set(safe_get_stop_words(lang) + localStopWords)
        #print (str(lang) + ' stop words was loaded successfully!')
    except:
        print ("Error! Stop words can not be loaded!")
        return defaultSWs   
    return defaultSWs


def load_default_stop_words(defaultLangs):
    defaultSWs = dict()
    #checking if list is empty
    if defaultLangs:
        for lang in defaultLangs.keys():
            if os.path.isfile(lang+'.txt'):
                localStopWords = (io.open(lang+'.txt', 'r', encoding="utf-8").read()).split()
            else:
                localStopWords = []
            try:
                defaultSWs[lang] = set(safe_get_stop_words(lang) + localStopWords)
                #print (str(lang) + ' stop words was loaded successfully!')
            except:
                print ("Error! Stop words can not be loaded!")
                return defaultSWs  
    else:
        print('The <defaultLangs> list is empty!')
        print("""Please, enter below at least one language and package name for language model downloading !
              For example, "en:nltk" or any other languages availаble at https://fasttext.cc/docs/en/language-identification.html 
              and corresponded packages for language models dowmloading availаble at https://pymorphy2.readthedocs.io/en/stable/index.html,
              https://www.nltk.org/book/ch05.html, https://spacy.io/models, https://stanfordnlp.github.io/stanza/available_models.html""")
        lang, package = input().split(":")
        defaultLangs = textProcessor.append_lang(defaultLangs, lang, package)
        defaultSWs = load_stop_words(defaultLangs, defaultSWs, lang)
    return defaultSWs
