# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:32:58 2021
Edited on Mon Oct  4 20:43:55 2021
Edited on Mon Feb  7 05:45:53 2022
Edited on Wed Feb 16 15:23:25 2022
Edited on Thu Feb 22 06:07:42 2022
Edited on Wed Feb 23 05:23:30 2022
Edited on Fri Feb 25 10:08:36 2022
Edited on Sat Feb 26 17:04:55 2022
Edited on Sun Feb 26 17:04:55 2022
Edited on Fri Mar  4 16:05:23 2022
Edited on Sun Mar  6 03:35:18 2022
Edited on Thu Mar  8 05:31:54 2022
Edited on Wed Mar  9 05:33:45 2022
Edited on Thu Mar 10 05:22:52 2022

@author: Олег Дмитренко

"""
import sys, os
from __modules__ import defaultConfigLoader, defaultModelsLoader, defaultSWsLoader, textProcessor, termsRanker

import time
t0 = time.time()

if __name__ == "__main__":
    inputFilePath = sys.argv[1]
    #if start script in python compiler mode, 'spyder' for example, than comemnt 2 line above and recomment 2 line below
    #inputFileDir = '/Users/dmytrenko.o/Documents/GitHub/termsExtractor/datasets/otbor4.txt'
    #inputFilePath = '/Users/dmytrenko.o/Documents/GitHub/narrativesExtractor/datasets/20210126_.txt'
    #outFileDir = '/Users/dmytrenko.o/Documents/GitHub/narrativesExtractor/results/'
    stdOutput = open("outlog.log", "a")
    sys.stderr = stdOutput
    sys.stdout = stdOutput

    defaultLangs = defaultConfigLoader.load_default_languages(os.getcwd())
    defaultSWs = defaultSWsLoader.load_default_stop_words(defaultLangs)
    nlpModels = defaultModelsLoader.load_default_models(defaultLangs)
    nGrams = defaultConfigLoader.load_default_ngrams(os.getcwd())
    
    with open(inputFilePath, "r", encoding="utf-8") as inputFlow:
        message = ""
        lines = (inputFlow.read()).splitlines()
        for line in lines:
            message += (line + '\n')
            if line == '***':
                message = message[:-4]
                if message:
                    sys.stdout = sys.__stdout__
                    print('<content>'+message+'</content>')
                    sys.stdout = stdOutput
                    message = message[0:defaultConfigLoader.default_int_value(os.getcwd(), 'maxMessLength')].lower()            
                    lang = textProcessor.lang_detect(message, defaultLangs, nlpModels, defaultSWs)
                    if (not defaultLangs[lang]):
                        message = ""
                        continue
                    if (defaultLangs[lang] == 'pymorphy2'):
                        dictTerms = textProcessor.pymorphy2_nlp(message, nlpModels[lang], defaultSWs[lang], nGrams)
                        NTerms = dict(zip(nGrams.keys(),[dictTerms[i] for i in nGrams]))
                        termsRanker.pymorphy2_most_freq_key_terms(NTerms, nGrams,
                                                                  defaultConfigLoader.default_int_value(os.getcwd(), 'maxNumNarratives'))
                    elif (defaultLangs[lang] == 'stanza'):
                        dictNTerms  = textProcessor.stanza_nlp(message, nlpModels[lang], defaultSWs[lang], nGrams)    
                        NTerms = dict(zip(nGrams.keys(),[dictNTerms[i] for i in nGrams]))
                        termsRanker.stanza_most_freq_key_terms(NTerms, nGrams,
                                                               defaultConfigLoader.default_int_value(os.getcwd(), 'maxNumNarratives'))
                    elif (not defaultLangs[lang]):
                        dictTerms = textProcessor.pymorphy2_nlp(message, nlpModels['uk'], defaultSWs['uk'], nGrams)    
                        Terms = dict(zip(nGrams.keys(),[dictTerms[i] for i in nGrams]))
                        termsRanker.pymorphy2_most_freq_key_terms(Terms, nGrams,
                                                                  defaultConfigLoader.default_int_value(os.getcwd(), 'maxNumNarratives'))
                
                message = ""
        inputFlow.close()
    print ("\nYou are lucky! The program successfully finished!\n")
    print (time.time() - t0)
    
