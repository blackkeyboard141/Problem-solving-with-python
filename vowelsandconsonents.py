# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 07:51:17 2019

@author: rasik
"""

def checkVowelsAndConsonents(sentence):
    sentence = sentence.lower()
    sentence = list(sentence)
    vowel = 0
    consonant=0
    
    for e in sentence:
        if( e == "a" or e=="e" or e=="i" or e=="o" or e=="u"):
            vowel = vowel+1
        elif (e!=" "):
            consonant = consonant+1
    
    return vowel, consonant



vowel, consonant = checkVowelsAndConsonents("My name is rasik")

print("Vowel: ",vowel," Consonant: ",consonant)