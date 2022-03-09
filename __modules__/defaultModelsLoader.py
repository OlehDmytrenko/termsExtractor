# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11:45:30 2022
Edited on Fri Feb 25 10:16:56 2022
Edited on Sat Feb 26 23:46:57 2022
Edited on Sun Mar 06 03:55:34 2022
Edited on Mon Mar  7 04:33:47 2022
Edited on Thu Mar  8 05:48:21 2022
Edited on Wed Mar  9 07:33:55 2022

@author: Олег Дмитренко

"""

from __modules__ import packagesInstaller
packages = ['subprocess', 'pymorphy2', 'nltk', 'spacy', 'stanza']
packagesInstaller.setup_packeges(packages)

import subprocess
from pymorphy2 import MorphAnalyzer
import nltk, spacy, stanza

def append_lang(defaultLangs, lang, package):
    try:
        defaultLangs[lang] = package
        #with open(dir_below()+"/config.json", "w") as configFile:
        #    try:
        #    except:
        #        pass
        #    configFile.close()
    except:
        print ('Unexpected Error while adding new languade to default list <defaultLangs>!')
    return defaultLangs

def download_model(defaultLangs, nlpModels, lang):
    if (defaultLangs[lang] == "pymorphy2"):
        try:
            subprocess.run('pip install -U pymorphy2-dicts-'+lang, shell=True)
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
    elif (defaultLangs[lang] == "nltk"):
        try:
            nltk.download(lang)
            print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))  
        except:
            print ("Error! '{0}' language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
            print ("There are no alternatives for {0} package downloading...".format(defaultLangs[lang]))
            return
        try:
            #nltk.data.path('/path/to/nltk_data/')
            #nlpModels[lang] = nltk
            print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))
        except:
            print ("Error! '{0}' language model for '{1}' package can not be loaded!".format(lang, defaultLangs[lang]))
            return
    elif (defaultLangs[lang] == "spacy"):
        try:
            subprocess.run("python -m spacy download {0}_core_news_sm".format(lang), shell=True)
            print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))     
        except:
            print ("Error! '{0}' language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
            print ("Alternative {0} package downloading...".format(defaultLangs[lang]))
            subprocess.run("python -m spacy download {0}_core_web_sm".format(lang), shell=True)
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
    elif (defaultLangs[lang] == "stanza"):
        try:
            stanza.download(lang)
            print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))  
        except:
            print ("Error! '{0} 'language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
            print ("There are no alternatives for {0} package downloading...".format(defaultLangs[lang]))
            return
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
                try:
                    subprocess.run('pip install -U pymorphy2-dicts-'+lang, shell=True)
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
            elif (defaultLangs[lang] == "nltk"):
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
            elif (defaultLangs[lang] == "spacy"):
                try:
                    subprocess.run("python -m spacy download {0}_core_news_sm".format(lang), shell=True)
                    print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))     
                except:
                    print ("Error! '{0}' language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
                    print ("Alternative {0} package downloading...".format(defaultLangs[lang]))
                    subprocess.run("python -m spacy download {0}_core_web_sm".format(lang), shell=True)
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
            elif (defaultLangs[lang] == "stanza"):
                try:
                    stanza.download(lang)
                    print ("'{0}' language model for '{1}' package was downloaded successfully!".format(lang, defaultLangs[lang]))  
                except:
                    print ("Error! '{0} 'language model for '{1}' package can not be dowloaded!".format(lang, defaultLangs[lang]))
                    print ("There are no alternatives for {0} package downloading...".format(defaultLangs[lang]))
                    return
                try:
                    nlpModels[lang] = stanza.Pipeline(lang, processors='tokenize,pos,lemma')
                    print ("'{0}' '{1}' model was loaded successfully!".format(lang, defaultLangs[lang]))
                except:
                    print ("Error! '{0}' language model for '{1}' package can not be loaded!".format(lang, defaultLangs[lang]))
                    print ("There are no alternatives for {0} package loading...".format(defaultLangs[lang]))
                    pass
    else:
        print('The <defaultLangs> list is empty!')
        print("""Please, enter below at least one language and package name for language model downloading !
              For example, "en:nltk" or any other languages availаble at https://fasttext.cc/docs/en/language-identification.html 
              and corresponded packages for language models dowmloading availаble at https://pymorphy2.readthedocs.io/en/stable/index.html,
              https://www.nltk.org/book/ch05.html, https://spacy.io/models, https://stanfordnlp.github.io/stanza/available_models.html""")
        lang, package = input().split(":")
        defaultLangs = append_lang(defaultLangs, lang, package)
        nlpModels = load_default_models(defaultLangs)
    return nlpModels
