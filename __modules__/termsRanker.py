# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12:55:31 2022
Edited on Sun Feb 26 23:54:43 2022
Edited on Thu Mar  8 06:25:44 2022
Edited on Wed Mar  9 09:03:15 2022

@author: Олег Дмитренко

"""      
import sys
from __modules__ import packagesInstaller
packages = ['nltk']
packagesInstaller.setup_packeges(packages)

from nltk import FreqDist

stdOutput = open("outlog.log", "a")
sys.stderr = stdOutput
sys.stdout = stdOutput

def stanza_most_freq(keyTerms, top):
    mostFreqKeyTerms = ''
    fdist = FreqDist(word.lower() for word in keyTerms)
    for (term, freq) in fdist.most_common(top):
        mostFreqKeyTerms = mostFreqKeyTerms + term  + ', ' 
    return mostFreqKeyTerms[:-2]

def stanza_most_freq_key_terms(Terms, nGrams, top):
    sys.stdout = sys.__stdout__
    for i in nGrams:
         print('<'+nGrams[i]+'>'+stanza_most_freq(Terms[i], top)+'</'+nGrams[i]+'>')  
    print('***')
    sys.stdout = stdOutput
    return

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def pymorphy2_most_freq(STerms, NTerms, top):
    mostFreqKeyTerms = ''
    mostFreqSTerms = []
    fdist = FreqDist(word.lower() for word in NTerms)
    for (term, freq) in fdist.most_common(top):
        mostFreqKeyTerms = mostFreqKeyTerms + str(get_key(STerms, term))  + ', ' 
        mostFreqSTerms.append(get_key(STerms, term))
    return mostFreqKeyTerms[:-2], mostFreqSTerms


def pymorphy2_most_freq_key_terms(Terms, nGrams, top):
    sys.stdout = sys.__stdout__
    for i in nGrams:
        mostFreqTerms, mostFreqSTerms = pymorphy2_most_freq(Terms[i][1], Terms[i][2], top)
        print('<'+nGrams[i]+'>'+mostFreqTerms+'</'+nGrams[i]+'>')
        mostFreqTerms = ''
        for sTerm in mostFreqSTerms:
            mostFreqTerms = mostFreqTerms + str(get_key(Terms[i][0], Terms[i][1][sTerm])) + ', ' 
        print('<Souerce '+nGrams[i]+'>'+mostFreqTerms[:-2]+'</Source '+nGrams[i]+'>')
    print('***')
    sys.stdout = stdOutput
    return
