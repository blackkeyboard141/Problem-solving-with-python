# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:41:16 2019

@author: rasik
"""

def maxmin(A):
    A.sort()
    arr=[A[0],A[len(A)-1]]
    return (arr)
    
  

A=[5,4,7,8,7,9]
print(maxmin(A))