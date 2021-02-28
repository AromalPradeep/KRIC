# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 01:42:32 2021

@author: Aromal Pradeep

"""

'''
KRIC - Kric is a Random Intellegent Calculator
==============================================

# Project for Mec Labs
'''

# Basic

# Imports

import time as t
#import random as r
#import re
from word2number import w2n 
from simpleeval import simple_eval

# NLTK
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Spell Checker
#from spellchecker import SpellChecker
#spell = SpellChecker()

# Date and Time
def today():
    return t.strftime("%d.%m.%y.%A.%H.%M").split('.')

# Main

while True:
    
    # User input
    i = input('user : ').lower()
    
    if i.lower() in ['break','end','quit']:
        break
    else:
        
        try:
            #case 0 : a Number entered
            try:
                o = (w2n.word_to_num(i))
            except:
                try:
                    #case 1 : Normal calculations (basic calculator)
                    '''Easy way was to use eval, but using eval has great risks as it could be used to potentially crack your system'''
                    o = simple_eval(i)
                    
                except:
                    try:
                        # clean sentence
                        words = [k for k in word_tokenize(i) if k not in stop_words]
                        o = words
                        for i in words:
                            if i in ['plus','add','addition','positive','summation']:
                                i = '+' 
                            elif i in ['minus','negative','subtraction','difference']:
                                i = '-'
                            elif i in ['x','multiply','product','times']:
                                i = '*'
                            elif i in ['divide','by']:
                                i = '/' 
                            elif i in ['power']:
                                i = '**'
                            else:
                                pass
                        
                    except:
                        #raise Exception()
                        pass
        except: # if in case of errors
            o = '<x_x> error...'
            
    # Output
    print('kric :',o)