# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:11:54 2019

@author: tsharris
"""

numbers = [10,9,8,7,6,5,4,3,2,1]#random list of numbers
print(numbers)

for k in range(len(numbers)-1):#for each index in the list - the last index
    for i in range(len(numbers)-1):#for each index in the list - the last index
        if (numbers[i] > numbers[i+1]):# if index i is > index i + 1 (consecutive index)
            temp = numbers[i] #Hold that index
            numbers[i] = numbers[i+1] #swap
            numbers[i+1] = temp#swap 
    
    print(numbers)