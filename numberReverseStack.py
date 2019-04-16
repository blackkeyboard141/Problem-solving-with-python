# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:16:15 2019

@author: rasik
"""

inputInt = 123456

inputString = str(inputInt)

print(type(inputString))

inputList = list(inputString)

stack =[]

for e in inputList:
    stack.append(e)
    
num = []
    
while(len(stack)!=0):
    num.append(stack.pop())    

print("".join(num))