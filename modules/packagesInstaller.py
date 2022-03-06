# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 06:56:18 2022
Edited on Sun Feb 26 22:04:35 2022

@author: Олег Дмитренко
"""

import sys
import importlib
import subprocess

def setup_packeges(packages):
    for package in packages:   
        if package in sys.modules:
            continue
            #print(f"{package!r} already in sys.modules")
        elif (spec := importlib.util.find_spec(package)) is not None:
            # If you choose to perform the actual import ...
            module = importlib.util.module_from_spec(spec)
            sys.modules[package] = module
            spec.loader.exec_module(module)
            #print(f"{package!r} has been imported")
        else:
            #print(f"Can't find the {package!r} module")
            try:
                # implement pip as a subprocess:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            except:
                print(f"Can't download the {package!r} module")
        