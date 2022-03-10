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
import sys
from __modules__ import packagesInstaller
packages = ['defaultConfigLoader', 'defaultModelsLoader', 'defaultSWsLoader', 'textProcessor', 'termsRanker']
packagesInstaller.setup_packeges(packages)
from __modules__ import defaultConfigLoader, defaultModelsLoader, defaultSWsLoader, textProcessor, termsRanker

if __name__ == "__main__":
    txtFileDir = sys.argv[1]
    #if start script not in CMD mode than comemnt line above and recomment line below
    #txtFileDir = '/Users/dmytrenko.o/Documents/GitHub/narrativesExtractor/datasets/otbor4.txt'
    #txtFileDir = '/Users/dmytrenko.o/Documents/GitHub/narrativesExtractor/datasets/20210126.txt'
    #txtFileDir = '/Users/dmytrenko.o/Documents/GitHub/narrativesExtractor/datasets/20210126_(2).txt'
    
    defaultLangs = defaultConfigLoader.load_default_languages()
    defaultSWs = defaultSWsLoader.load_default_stop_words(defaultLangs)
    nlpModels = defaultModelsLoader.load_default_models(defaultLangs)
    nGrams = defaultConfigLoader.load_default_ngrams()    
    
    with open(txtFileDir, "r", encoding="utf-8") as inputFlow:
        message = ""
        lines = (inputFlow.read().lower()).splitlines()
        for line in lines:
            message += (line + ' ')
            if line == '***':
                message = message[:-4]
                if message:
                    print (message)
                    message = (message.replace("\n"," "))[0:defaultConfigLoader.default_int_value('maxMessLength')] #delete all \n from input message              
                    lang = textProcessor.lang_detect(message, defaultLangs, nlpModels, defaultSWs)
                    if (not defaultLangs[lang]):
                        message = ""
                        continue 
                    if (defaultLangs[lang] == 'pymorphy2'):
                        Words, SBigrams, Bigrams, SThreegrams, Threegrams  = textProcessor.pymorphy2_nlp(message, nlpModels[lang], defaultSWs[lang])    
                        SWords = dict(list(zip(Words, Words)))
                        termsRanker.pymorphy2_most_freq_key_terms(SWords, Words, SBigrams, Bigrams, SThreegrams, Threegrams,
                                                        defaultConfigLoader.default_int_value('maxNumNarratives'))
                    elif (defaultLangs[lang] == 'stanza'):
                        Words, Bigrams, Threegrams  = textProcessor.stanza_nlp(message, nlpModels[lang], defaultSWs[lang])    
                        termsRanker.stanza_most_freq_key_terms(Words, Bigrams, Threegrams,
                                                    defaultConfigLoader.default_int_value('maxNumNarratives'))
                message = ""
        inputFlow.close()
