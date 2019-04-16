# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


"""

def palindrome(check):
    reverse = []
    x= len(check)-1
    p=True
    i=x
    
    
    while(i>=0):
            reverse.append(check[i])
            i=i-1
            
    a = "".join(reverse)   
     
    if(a!=check):
        p=False
    
    return p
 
        
    
   
    




print(palindrome("ogo"))

