# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 23:36:12 2019

@author: rasik
"""

def binarySearch(arr, start, finish, num):
    
    mid = int((start + (finish-1))/2)
 
    
    if(arr[mid] == num):
        print(mid)
        return mid
    
    elif (num > arr[mid]):
        print (mid)
        return binarySearch(arr, mid+1 , finish, num)
    
    elif(num< arr[mid]):
        print(mid)
        return binarySearch(arr, start, mid-1, num)
        
        
arr = [11,24,35,46,55,62,73,86,92,100]

start = 0
finish = len(arr)-1
num = 24

position = binarySearch(arr, start, finish, num )

print(position)