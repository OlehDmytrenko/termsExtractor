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

def most_freq(keyTerms, top):
    mostFreqKeyTerms = ''
    fdist = FreqDist(word.lower() for word in keyTerms)
    for (term, freq) in fdist.most_common(top):
        mostFreqKeyTerms = mostFreqKeyTerms + term  + ', ' 
    return mostFreqKeyTerms[:-2]

def most_freq_key_terms(Words, Bigrams, Threegrams, top):
    print (most_freq(Words,top))
    print (most_freq(Bigrams, top))
    print (most_freq(Threegrams,top))
    print ('***')
    return

def most_freq_key_terms_(nGrams, top):
    for keyTerms in nGrams:
        print (most_freq(keyTerms,top))
    print ('***')
    return
