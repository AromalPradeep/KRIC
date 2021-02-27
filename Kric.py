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
#import re
from word2number import w2n 
from simpleeval import simple_eval

# Main

while True:
    
    # User input
    i = input('user : ')
    
    if i == 'break':
        break
    else:
        #case 0 : a Number entered
        try:
            o = (w2n.word_to_num(i))
        except:
            
            #case 1 : Normal calculations (basic calculator)
            '''Easy way was to use eval, but using eval has great risks as it could be used to potentially crack your system'''
            o = simple_eval(i)
            
            
    # Output
    print('kric :',o)
#    else:
#        print('X_X Error...')
