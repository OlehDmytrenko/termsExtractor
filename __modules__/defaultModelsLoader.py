# -*- coding: utf-8 -*-
"""

@author: Олег Дмитренко

"""

from __modules__ import packagesInstaller, textProcessor
packages = ['subprocess', 'pymorphy2', 'nltk', 'spacy', 'stanza']
packagesInstaller.setup_packeges(packages)

import subprocess
from pymorphy2 import MorphAnalyzer
import nltk, spacy, stanza

def pymorphy2_model_loader(defaultLangs, nlpModels, lang):
    try:
        subprocess.run("pip install -U pymorphy2-dicts-"+lang+"| grep -v 'already satisfied'", shell=True)
        print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))
    except:
        print ("Error! '{0}' language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
        print ("There are no alternatives for {0} package downloading...".format(defaultLangs[lang]))
        return
    try:
        nlpModels[lang] = MorphAnalyzer(lang = lang)
        print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))    
    except:
        print ("Error! '{0}' language model for '{1}' package can not be loaded!".format(lang, defaultLangs[lang]))
        return
    return nlpModels
 
def nltk_model_loader(defaultLangs, nlpModels, lang):
    try:
        nltk.download(lang)
        print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))  
    except:
        print ("Error! '{0}' language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
        print ("There are no alternatives for {0} package downloading...".format(defaultLangs[lang]))
        return
    try:
        #nltk.data.path('/Users/dmytrenko.o/nltk_data')
        nlpModels[lang] = nltk
        print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))
    except:
        print ("Error! '{0}' language model for '{1}' package can not be loaded!".format(lang, defaultLangs[lang]))
        return
    return nlpModels

def spacy_model_loader(defaultLangs, nlpModels, lang):
    try:
        subprocess.run("python -m spacy download {0}_core_news_sm | grep -v 'already satisfied'".format(lang), shell=True)
        print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))     
    except:
        print ("Error! '{0}' language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
        print ("Alternative {0} package downloading...".format(defaultLangs[lang]))
        subprocess.run("python -m spacy download {0}_core_web_sm | grep -v 'already satisfied'".format(lang), shell=True)
        print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))
        pass
    try:
        nlpModels[lang] = spacy.load(lang+"_core_web_sm")
        print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))
    except:
        print ("Error! '{0}' language model for '{1}' package can not be loaded!".format(lang, defaultLangs[lang]))
        print ("Alternative {0} package loading...".format(defaultLangs[lang]))
        nlpModels[lang] = spacy.load(lang+"_core_news_sm")
        print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))
        pass
    return nlpModels

def stanza_model_loader(defaultLangs, nlpModels, lang):
    try:
        stanza.download(lang)
        print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))  
    except:
        print ("Error! '{0} 'language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
        print ("'uk' 'Pymorphy2' model instead '{0}' is downloading as alternative...".format(defaultLangs[lang]))
        print ("ʼukʼ 'Pymorphy2' model is loading...")
        nlpModels[lang] = pymorphy2_model_loader(defaultLangs, nlpModels, 'uk')
        defaultLangs = textProcessor.append_lang(defaultLangs, lang, 'pymorphy2')
        return nlpModels
    try:
        nlpModels[lang] = stanza.Pipeline(lang, processors='tokenize,pos,lemma')
        print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))
    except:
        print ("Error! '{0}' language model for '{1}' package can not be loaded!".format(lang, defaultLangs[lang]))
        print ("There are no alternatives for {0} package loading...".format(defaultLangs[lang]))
        pass
    return nlpModels

def load_default_models(defaultLangs):
    nlpModels = dict()
    #checking if list is empty
    if defaultLangs:
        for lang in defaultLangs.keys():
            if (defaultLangs[lang] == "pymorphy2"):
                nlpModels = pymorphy2_model_loader(defaultLangs, nlpModels, lang)
            elif (defaultLangs[lang] == "nltk"):
                nlpModels = nltk_model_loader(defaultLangs, nlpModels, lang)
            elif (defaultLangs[lang] == "spacy"):
                nlpModels = spacy_model_loader(defaultLangs, nlpModels, lang)
            elif (defaultLangs[lang] == "stanza"):
                nlpModels = stanza_model_loader(defaultLangs, nlpModels, lang)
    else:
        print('The <defaultLangs> list is empty!')
        print("""Please, enter below at least one language and package name for language model downloading !
              For example, "en:nltk" or any other languages availаble at https://fasttext.cc/docs/en/language-identification.html 
              and corresponded packages for language models dowmloading availаble at https://pymorphy2.readthedocs.io/en/stable/index.html,
              https://www.nltk.org/book/ch05.html, https://spacy.io/models, https://stanfordnlp.github.io/stanza/available_models.html""")
        lang, package = input().split(":")
        defaultLangs = textProcessor.append_lang(defaultLangs, lang, package)
        nlpModels = load_default_models(defaultLangs)
    return nlpModels
