# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:19:21 2019

@author: rasik
"""

stackInput =[]

brackets ={")":"(" , "}":"{", "]":"["}
bracket = {"(":")" , "{":"}" , "[":"]"}

inputString = ""

stackInput = list(inputString)


stackCheck = []


try:
    for e in stackInput:
        if len(stackCheck)!=0 and e == bracket[stackCheck[-1]]:
            stackCheck.pop()
        elif len(stackCheck)==0 or e != bracket[stackCheck[-1]]:
            stackCheck.append(e)

except:
    print("false")
     
        
if len(stackCheck) == 0:
    print("true")
