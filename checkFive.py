# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:42:19 2019

@author: rasik
"""

def repeatedFive(arr):
    checkFive = {}
    
    for e in arr:
        if(e not in checkFive):
            checkFive[e] = 1;
        elif(e in checkFive):
            checkFive[e] = checkFive[e] +1
            if (checkFive[e] == 5):
                return e
        
    
        
    
            
            
arr = [1,2,3,4,5,1,23,4,512,5,12,4,5,12,34,5,12,25,68,6,8,45,5]            
print(repeatedFive(arr))