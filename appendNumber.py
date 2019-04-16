# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:54:35 2019

@author: rasik
"""

def numberAppend(n1, n2):
    length = len(str(n2))-1
    factor = 10
    
    
    while(length>0):
        factor = factor*10
        length = length-1
        
        
    final = (n1*factor)+n2
    
    return final


print(numberAppend(581,76))
    
    
    
    
    
    
    
