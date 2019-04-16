# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:32:03 2019

@author: rasik
"""

def rearrange(Str):
    Str = list(Str)
    
    mapping = {}
    
    for e in Str:
        if(e not in mapping):
            mapping[e] = 1
        else:
            mapping[e] = mapping[e]+1
    
    x= len(Str)-1
    
    rearranged = []
    
    while(x>=0):
        for e in mapping:
            if mapping[e]!=0:
                rearranged.append(e)
                mapping[e] = mapping[e]-1
        x=x-1
        
    return rearranged


Str = "RRRRBBG"

print("".join(rearrange(Str)))