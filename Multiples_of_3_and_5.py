# -*- coding: utf-8 -*-
"""
Created on Mon May  1 01:57:01 2017

@author: Марианна
"""

def solution(number):
    '''
    It returns the sum of all the multiples of 3 or 5 below the number passed in.
    Note: If the number is a multiple of both 3 and 5, only count it once.
    '''
    new_number = []
    num3 = 0
    num5 = 0
    sum = 0
    for i in range(number):
        num3 = i*3
        if num3 < number:
            if num3 not in new_number:  
                new_number.append(num3)
        num5 = i*5
        if num5 < number:
            if num5 not in new_number:
                new_number.append(num5)
    for i in new_number:
        sum += i
    return sum

print("The sum is", solution(10))       