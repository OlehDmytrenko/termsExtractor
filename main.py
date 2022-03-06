# -*- coding: utf-8 -*-
"""
Created on Wed May 5 10:32:58 2021
Edited on Mon Oct 4 20:43:55 2021
Edited on Mon Feb 7 05:45:53 2022
Edited on Wed Feb 16 15:23:25 2022
Edited on Thu Feb 22 06:07:42 2022
Edited on Wed Feb 23 05:23:30 2022
Edited on Fri Feb 25 10:08:36 2022
Edited on Sat Feb 26 17:04:55 2022
Edited on Sun Feb 26 17:04:55 2022
Edited on Fri Mar 04 16:05:23 2022
Edited on Sun Mar 06 03:35:18 2022

@author: Олег Дмитренко

"""
import os, subprocess, sys
subprocess.run('python -m venv '+os.getcwd()+'/modules/', shell=True)
from modules import defaultLoader, textProcessor, termsRanker

if __name__ == "__main__":
    txtFileDir = sys.argv[1]
    #if start script not in CMD mode than comemnt line above and recomment line below
    #txtFileDir = '/Users/dmytrenko.o/Documents/GitHub/narrativesExtractor/datasets/otbor4.txt'
    
    defaultLangs = defaultLoader.load_default_languages()
    exceptedLangs = defaultLoader.load_except_languages()
    nlpModels = defaultLoader.load_default_models(defaultLangs)
    stopWords = defaultLoader.load_default_stop_words(defaultLangs)
    
    with open(txtFileDir, "r", encoding="utf-8") as file:
        messages = (file.read().lower()).split('***')
        for message in messages:
            if message:
                message = message.replace("\n"," ") #delete all \n from input message
                print (message)               
            
                lang = textProcessor.lang_detect(message, defaultLangs, nlpModels, stopWords)
                if (lang in exceptedLangs):
                   continue 
                Words, Bigrams, Threegrams  = textProcessor.nl_processing(message, nlpModels[lang], stopWords[lang])    
                termsRanker.most_freq_key_terms(Words, Bigrams, Threegrams)
