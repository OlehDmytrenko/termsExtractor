# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12:55:31 2022
Edited on Sun Feb 26 23:54:43 2022
Edited on Thu Mar  8 06:25:44 2022
Edited on Wed Mar  9 09:03:15 2022

@author: Олег Дмитренко

"""      
from __modules__ import packagesInstaller
packages = ['nltk']
packagesInstaller.setup_packeges(packages)

from nltk import FreqDist

def stanza_most_freq(keyTerms, top):
    mostFreqKeyTerms = ''
    fdist = FreqDist(word.lower() for word in keyTerms)
    for (term, freq) in fdist.most_common(top):
        mostFreqKeyTerms = mostFreqKeyTerms + term  + ', ' 
    return mostFreqKeyTerms[:-2]

def stanza_most_freq_key_terms(Words, Bigrams, Threegrams, top, outFlow):
    outFlow.write(stanza_most_freq(Words,top)+'\n')
    outFlow.write(stanza_most_freq(Bigrams, top)+'\n')
    outFlow.write(stanza_most_freq(Threegrams,top)+'\n')
    outFlow.write('***'+'\n')
    return

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def pymorphy2_most_freq(keyTerms, STerms, top):
    mostFreqKeyTerms = ''
    fdist = FreqDist(word.lower() for word in keyTerms)
    for (term, freq) in fdist.most_common(top):
        mostFreqKeyTerms = mostFreqKeyTerms + str(get_key(STerms, term))  + ', ' 
    return mostFreqKeyTerms[:-2]

def pymorphy2_most_freq_key_terms(SWords, Words, SBigrams, Bigrams, SThreegrams, Threegrams, top, outFlow):
    outFlow.write(pymorphy2_most_freq(Words, SWords, top)+'\n')
    outFlow.write(pymorphy2_most_freq(Bigrams, SBigrams, top)+'\n')
    outFlow.write(pymorphy2_most_freq(Threegrams, SThreegrams, top)+'\n')
    outFlow.write('***'+'\n')
    return

#def most_freq_key_terms_(nGrams, top):
#    for keyTerms in nGrams:
#        print (stanza_most_freq(keyTerms,top))
#    print ('***')
#    return
