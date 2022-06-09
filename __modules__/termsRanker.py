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

def CoordBigram(mostFreqTerms):
    CoordMostFreqTerms = ''
    for bigram in mostFreqTerms.split(", "):
        nw1, nw2 = bigram.split("_")
        if (nw2[-1:] == "а") or (nw2[-2:] == "ль"):
            if (nw1[-3:] == "вой"):
                nw1 = nw1[:-3]+"вая"
            elif(nw1[-3:] == "ный"):
                nw1 = nw1[:-3]+"ная"
            elif(nw1[-3:] == "кий"):
                nw1 = nw1[:-3]+"кая"
            elif(nw1[-2:] == "ый"):
                nw1 = nw1[:-2]+"ая"
        elif (nw2[-1:] == "я"):
            if (nw1[-3:] == "вой"):
                nw1 = nw1[:-3]+"вая"
            elif(nw1[-3:] == "ный"):
                nw1 = nw1[:-3]+"ная"
            elif(nw1[-3:] == "гий"):
                nw1 = nw1[:-3]+"гая"
            elif(nw1[-3:] == "ший"):
                nw1 = nw1[:-3]+"шая"
            elif(nw1[-3:] == "щий"):
                nw1 = nw1[:-3]+"щая"
        elif (nw2[-2:] == "ие") or (nw2[-1:] == "o"):
             if (nw1[-2:] == "ый"):
                 nw1 = nw1[:-2]+"ое"
             elif(nw1[-2:] == "ой"):
                 nw1 = nw1[:-2]+"ое"
             elif(nw1[-3:] == "ший"):
                 nw1 = nw1[:-3]+"шее"
             elif(nw1[-3:] == "щий"):
                 nw1 = nw1[:-3]+"щее"
             elif(nw1[-3:] == "кий"):
                 nw1 = nw1[:-3]+"кое"
        CoordMostFreqTerms = CoordMostFreqTerms + nw1+"~"+nw2 + ', ' 
    return CoordMostFreqTerms[:-2]

def pymorphy2_most_freq(keyTerms, top):
    mostFreqKeyTerms = ''
    fdist = FreqDist(word.lower() for word in keyTerms)
    for (term, freq) in fdist.most_common(top):
        mostFreqKeyTerms = mostFreqKeyTerms + term  + ', ' 
    return mostFreqKeyTerms[:-2]


def pymorphy2_most_freq_key_terms(NTerms, nGrams, top):
    sys.stdout = sys.__stdout__
    for i in nGrams:
        mostFreqTerms = pymorphy2_most_freq(NTerms[i], top)
        if nGrams[i] == "Bigrams":
            mostFreqTerms = CoordBigram(mostFreqTerms)
        print('<'+nGrams[i]+'>'+mostFreqTerms+'</'+nGrams[i]+'>')
    print('***')
    sys.stdout = stdOutput
    return
