# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:55:22 2019

@author: rasik
"""

def secondLargestandSecondsmallest(arr):
    
    sortedlist = sorted(arr)
    
    return sortedlist[1], sortedlist[len(sortedlist)-2]
    
    
    
    
    
    
    
    
    
    
arr = [9,2,3,4,5,6,7,8,1]
small, large  = secondLargestandSecondsmallest(arr)
print("second largest", large, "second smallest" , small)