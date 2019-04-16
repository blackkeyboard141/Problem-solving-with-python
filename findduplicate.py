# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:21:14 2019

@author: rasik
"""

def findDuplicate(A):
    arr = {}
    
    for e in A:
        if e not in arr:
            arr[e]=1
        else:
            arr[e] = arr[e]+1
            
    
    duplicates = []
    for e in arr:
        if arr[e]>1:
            duplicates.append(e)
    
    return duplicates
    
    

A= [2,2, 4, 5, 6,1,1]
print(findDuplicate(A))