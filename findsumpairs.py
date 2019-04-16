# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:55:20 2019

@author: rasik
"""

def findsumpair(A, sum):
    n = len(A)-1
    
    m = {}
    
    
    
    for e in A:
        if e not in arr:
            arr[e]=1
        else:
            arr[e] = arr[e]+1
            
    twice_count = 0
  
    # Iterate through each element and increment 
    # the count (Notice that every pair is  
    # counted twice) 
    for i in range(0, n): 
      
        twice_count += m[sum - arr[i]]  
  
        # if (arr[i], arr[i]) pair satisfies the 
        # condition, then we need to ensure that 
        # the count is  decreased by one such  
        # that the (arr[i], arr[i]) pair is not 
        # considered 
        if (sum - arr[i] == arr[i]): 
            twice_count -= 1
      
    # return the half of twice_count 
    return int(twice_count / 2) 
    
    
    
    
    
    
    
    
arr = [1, 5, 7, -1, 5]  
sum = 6

print(findsumpair(arr, sum))