# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:14:22 2019

@author: rasik
"""


def findmissing(A):
    fakesum = 0
    n = len(A)
    sum = int(((n+1)*(n+2))/2)
    
    for element in A:
        fakesum = fakesum+element

    return sum-fakesum



A = [1, 2, 4, 5, 6] 
print(findmissing(A))