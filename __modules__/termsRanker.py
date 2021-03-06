# -*- coding: utf-8 -*-
"""

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
        nw1, nw2 = bigram.split('~')
        if (nw2[-1:] == "а"):
            if (nw1[-3:] == "вой"):
                nw1 = nw1[:-3]+"вая"
            elif(nw1[-3:] == "ный"):
                nw1 = nw1[:-3]+"ная"
            elif(nw1[-3:] == "кий"):
                nw1 = nw1[:-3]+"кая"
            elif(nw1[-2:] == "ый"):
                nw1 = nw1[:-2]+"ая"
        elif (nw2[-2:] == "ль"):
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
        elif (nw2[-3:] == "сть"):
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
            elif(nw1[-3:] == "кий"):
                nw1 = nw1[:-3]+"кая"
        elif (nw2[-2:] == "ие"):
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
        elif (nw2[-1:] == "о"):
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

        CoordMostFreqTerms = CoordMostFreqTerms + nw1+'~'+nw2 + ', ' 
    return CoordMostFreqTerms[:-2]

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
        if (nGrams[i] == "Bigrams") and mostFreqTerms:
            mostFreqTerms = CoordBigram(mostFreqTerms)
        elif nGrams[i] == "Threegrams":
            mostFreqTerms = ''
            for sTerm in mostFreqSTerms:
                mostFreqTerms = mostFreqTerms + str(get_key(Terms[i][0], Terms[i][1][sTerm])) + ', ' 
            mostFreqTerms = mostFreqTerms[:-2]
        print('<'+nGrams[i]+'>'+mostFreqTerms+'</'+nGrams[i]+'>')
    print('***')
    sys.stdout = stdOutput
    return
