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

# The GUI interface

# Basic

# Imports

import time
#import random as r
#import re
from word2number import w2n 
from simpleeval import simple_eval

# NLTK
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize

# Spell Checker
#from spellchecker import SpellChecker
#spell = SpellChecker()

# Kivy
import kivy
from kivy.app import App
from kivy.config import Config 
from kivy.core.window import Window

# UIX
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.pagelayout import PageLayout 
from kivy.clock import Clock

# Date and Time
def today():
    return time.strftime("%d.%m.%y.%A.%H.%M").split('.')

# Base
class base(GridLayout):
    
    '''def __init__(self):
        pass'''
        
    #def kill(self):
    #   exit()
        
    def Minus_app_button(self):
        App.get_running_app().root_window.minimize()
        
    def MaxiMin_app_button(self):
        if Window.fullscreen:
            Window.fullscreen = False
        else:
            Window.fullscreen = True
        
    def close_app_button(self):
        kricApp.stop()
    
    def Time(self):
        return time.strftime('[b]%H[/b]:%M:%S')
    
    # Think - The main code
    def think(self,i):    
        # User input
        #i = entry.text
        #i = self.root.ids.entry.text 
            
        if i.lower() in ['break','end','quit']:
            exit()
        
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
                            i = i.lower()
                            words = [k for k in word_tokenize(i) if k not in stop_words]
                            o = words
                            
                        except:
                            #raise Exception()
                            pass
            except: # if in case of errors
                o = '<x_x> error...'
                    
            # Output
            self.ids.output.text = str(o)
            self.ids.entry.text = ''
    
class KricApp(App):
    
    def build(self):
        
        # Layout dimensions
        #Config.set('graphics', 'resizable', False)
        #Config.set('graphics', 'borderless', 'True')
        #Config.set('graphics', 'width', '400') 
        #Config.set('graphics', 'height', '300') 

        Window.size = (300,300)
        Window.borderless = True
        
        return base()    
    
# Run the App 
if __name__ == "__main__": 
    kricApp = KricApp() 
    kricApp.run() 