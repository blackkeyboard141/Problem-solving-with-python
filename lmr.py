# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:57:50 2019

@author: rasik
"""

"""
Given a length n, l, r of a string “lllmmmmmmrrr”, write a function to calculate the length m of middle sub-string 
where n is the length of whole string, l is the length of left sub-string, r is the length of right sub-string 
and l = r. (l+r=m, n=m+l+r)

"""

def findLengthOfM(Str,l):
    ending = len(Str)-l
    
    return Str[l:ending]


Str = "llmmmmrr"
l=2
print(findLengthOfM(Str,l))