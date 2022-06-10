# -*- coding: utf-8 -*-
"""

@author: dmytrenko.o
"""
import os
from __modules__ import packagesInstaller
packages = ['json']
packagesInstaller.setup_packeges(packages)

import json

def dir_below():
    curFolder = os.path.abspath(os.getcwd()).replace(os.path.dirname(os.path.abspath(os.curdir)),"")
    dirBelow = os.path.abspath(os.curdir).replace(curFolder, "")
    return dirBelow

def load_default_ngrams(configPath):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            try:
                ngrams = {list(langModel.keys())[0] : langModel[list(langModel.keys())[0]]
                                for langModel in jsonConfig["nGrams"]}
            except AttributeError:
                pass
            configFile.close()
    except:
        print ("Error! Ngrams can't be reading! Please, check a field {0} in config.json".format("ngrams"))
        ngrams = {"1" : "Words", "2" : "Bigrams", "3" : "Threegrams"}
    return ngrams

def default_int_value(configPath, key):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            messageLength = int(jsonConfig[key])
            configFile.close()
    except:
        print ("Error! Max Messages Length can't be reading! Please, check a key {0} in config.json".format(key))
    return messageLength

def load_default_languages(configPath):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            try:
                defaultLangs = {list(langModel.keys())[0] : langModel[list(langModel.keys())[0]]
                                for langModel in jsonConfig["langConfig"]}
            except AttributeError:
                pass
            configFile.close()
    except:
        print ("Error! Default languages can't be reading! Please, check a field {0} in config.json".format("langConfig"))
        defaultLangs = {"uk": "pymorphy2", "ru": "pymorphy2", "en" : "stanza", "kv": "", "tl": "", "bcl": "",
                        "xal": "", "ba": "", "ga": ""}
        pass
    return defaultLangs
