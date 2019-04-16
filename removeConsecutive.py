# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 08:34:51 2019

@author: rasik
"""

def removeConsecutive(sentence):
    
    sentence = sentence.lower()
    
    sentence = list(sentence)
    
    buffer = ""
    
    for idx, e in enumerate(sentence):
        if(buffer == ""):
            buffer = e
        elif(buffer != "" and buffer == e):
            sentence[idx] = ""
        
        buffer = e
            
    
    return sentence
     
    
    
print("".join(removeConsecutive("aaammabbbjjkiuiieqo")))