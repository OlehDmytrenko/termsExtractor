# -*- coding: utf-8 -*-
"""

@author: Олег Дмитренко

"""
from __modules__ import packagesInstaller
packages = ['fasttext', 'nltk']
packagesInstaller.setup_packeges(packages)

import fasttext
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from __modules__ import defaultModelsLoader, defaultSWsLoader

def stanza_built_words(sent, NWords, stopWords):
    WordsTags = []
    for word in sent.words:
        nword = word.lemma
        tag = word.upos
        if tag == 'PROPN':
            tag = 'NOUN'
        WordsTags.append((nword,tag))
        if (nword not in stopWords) and (tag == 'NOUN'): 
            NWords.append(nword)
    return WordsTags, NWords

def stanza_built_bigrams(WordsTags, NBigrams, stopWords):
    for i in range(1, len(WordsTags)):
        w1 = WordsTags[i-1][0] 
        w2 = WordsTags[i][0]
        t1 = WordsTags[i-1][1]
        t2 = WordsTags[i][1]
        if (t1 == 'ADJ') and (t2 == 'NOUN') and (w1 not in stopWords) and (w2 not in stopWords):
            NBigrams.append(w1+'_'+w2)
    return NBigrams

def stanza_built_threegrams(WordsTags, NThreegrams, stopWords):
    for i in range(2, len(WordsTags)):
        w1 = WordsTags[i-2][0]
        w2 = WordsTags[i-1][0]
        w3 = WordsTags[i][0]
        t1 = WordsTags[i-2][1]
        t2 = WordsTags[i-1][1]
        t3 = WordsTags[i][1]
        if (t1 == 'NOUN') and ((t2 == 'CCONJ') or (t2 == 'ADP')) and (t3 == 'NOUN') and (w1 not in stopWords) and (w3 not in stopWords):
            NThreegrams.append(w1+'_'+w2+'_'+w3)
        elif (t1 == 'ADJ') and (t2 == 'ADJ') and (t3 == 'NOUN') and (w1 not in stopWords) and (w2 not in stopWords) and (w3 not in stopWords):
            NThreegrams.append(w1+'_'+w2+'_'+w3)    
    return NThreegrams

def stanza_nlp(text, nlpModel, stopWords, nGrams):
    NWords = []
    NBigrams = []
    NThreegrams = []
    doc = nlpModel(text)
    sents = doc.sentences
    for sent in sents:
        WordsTags, NWords = stanza_built_words(sent, NWords, stopWords)
        if ('Bigrams' in nGrams.values()) and (len(WordsTags)>2):
            NBigrams = stanza_built_bigrams(WordsTags, NBigrams, stopWords)
        if ('Threegrams' in nGrams.values()) and (len(WordsTags)>3):
            NThreegrams = stanza_built_threegrams(WordsTags, NThreegrams, stopWords)
    return {"1" : NWords, "2" : NBigrams, "3" : NThreegrams}

def pymorphy2_built_words(sent, Words, NWords, nlpModel, stopWords):
    WordsTags = []
    Words = []
    words = word_tokenize(sent)
    for word in words:
        nword = nlpModel.normal_forms(word)[0]
        tag = str((nlpModel.parse(word)[0]).tag.POS)
        if tag == 'NPRO':
            tag = 'NOUN'
        WordsTags.append((nword,tag))
        Words.append(word)
        if (nword not in stopWords) and (tag == 'NOUN'): 
            NWords.append(nword)
    return WordsTags, Words, NWords

def CoordBigram(Bigrams, nw1, nw2, nlpModel):
    adjMorph = nlpModel.parse(nw1)[0]
    nounMorph = nlpModel.parse(nw2)[0]
    nounGender = nounMorph.tag.gender
    if nounGender == "masc":   
        Bigrams[nw1+'_'+nw2] = nw1+'_'+nw2
    else:
        Bigrams[adjMorph.inflect({nounGender}).word+'_'+nw2] = nw1+'_'+nw2
      
def pymorphy2_built_bigrams(WordsTags, Words, Bigrams, NBigrams, nlpModel, stopWords):
    for i in range(1, len(WordsTags)):
        nw1 = WordsTags[i-1][0] 
        nw2 = WordsTags[i][0]
        w1 = Words[i-1]
        w2 = Words[i]
        t1 = WordsTags[i-1][1]
        t2 = WordsTags[i][1]
        if (t1 == 'ADJF') and (t2 == 'NOUN') and (nw1 not in stopWords) and (nw2 not in stopWords):
            NBigrams.append(nw1+'_'+nw2)
            try:
                #CoordBigram(Bigrams, nw1, nw2, nlpModel)
                Bigrams[w1+'_'+w2] = nw1+'_'+nw2
            except:
                Bigrams[w1+'_'+w2] = nw1+'_'+nw2
                continue
    return Bigrams, NBigrams

def pymorphy2_built_threegrams(WordsTags, Words, Threegrams, SThreegrams, NThreegrams, stopWords):
    for i in range(2, len(WordsTags)):
        nw1 = WordsTags[i-2][0]
        nw2 = WordsTags[i-1][0]
        nw3 = WordsTags[i][0]
        w1 = Words[i-2]
        w2 = Words[i-1]
        w3 = Words[i]
        t1 = WordsTags[i-2][1]
        t2 = WordsTags[i-1][1]
        t3 = WordsTags[i][1]
        if (t1 == 'NOUN') and ((t2 == 'CCONJ') or (t2 == 'PREP')) and (t3 == 'NOUN') and (nw1 not in stopWords) and (nw3 not in stopWords):
            NThreegrams.append(nw1+'_'+nw2+'_'+nw3)
            SThreegrams[nw1+'_'+nw2+'_'+w3] = nw1+'_'+nw2+'_'+nw3
            Threegrams[w1+'_'+w2+'_'+w3] = nw1+'_'+nw2+'_'+nw3
        elif (t1 == 'ADJF') and (t2 == 'ADJF') and (t3 == 'NOUN') and (nw1 not in stopWords) and (nw2 not in stopWords) and (nw3 not in stopWords):
            NThreegrams.append(nw1+'_'+nw2+'_'+nw3)
            SThreegrams[nw1+'_'+nw2+'_'+w3] = nw1+'_'+nw2+'_'+nw3
            Threegrams[w1+'_'+w2+'_'+w3] = nw1+'_'+nw2+'_'+nw3
    return Threegrams, SThreegrams, NThreegrams

def pymorphy2_nlp(text, nlpModel, stopWords, nGrams):
    Words = dict()
    Bigrams = dict()
    Threegrams = dict()
    SThreegrams = dict()
    NWords = []
    NBigrams = []
    NThreegrams = []
    sents = sent_tokenize(text)
    for sent in sents:
        WordsTags, Words, NWords = pymorphy2_built_words(sent, Words, NWords, nlpModel, stopWords)
        if ('Bigrams' in nGrams.values()) and (len(WordsTags)>2):
            Bigrams, NBigrams = pymorphy2_built_bigrams(WordsTags, Words, Bigrams, NBigrams, nlpModel, stopWords)
        if ('Threegrams' in nGrams.values()) and (len(WordsTags)>3):
            Threegrams, SThreegrams, NThreegrams = pymorphy2_built_threegrams(WordsTags, Words, Threegrams, SThreegrams, NThreegrams, stopWords)
    Words = dict(list(zip(NWords, NWords)))
    SWords = dict(list(zip(NWords, NWords)))
    SBigrams = dict(list(zip(NBigrams, NBigrams)))
    return {"1" : (Words, SWords, NWords), "2" : (Bigrams, SBigrams, NBigrams), "3" : (Threegrams, SThreegrams, NThreegrams)}

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

def lang_detect(message, defaultLangs, nlpModels, stopWords):
    lidModel = fasttext.load_model('lid.176.ftz')
    message = message.replace("\n", " ")
    #Check if all the characters in the text are whitespaces
    if message.isspace():
        return 'uk'
    else:
        try:
            # get first item of the prediction tuple, then split by "__label__" and return only language code
            lang = lidModel.predict(message)[0][0].split("__label__")[1]
        except:
            return "uk"
    if (lang not in defaultLangs):
        try:
            nlpModels = defaultModelsLoader.stanza_model_loader(defaultLangs, nlpModels, lang)
        except:
            return "uk"
        defaultSWsLoader.load_stop_words(defaultLangs, stopWords, lang)
    return lang
