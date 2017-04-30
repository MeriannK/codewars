# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 14:42:54 2017

@author: Марианна
"""

'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

def unique_in_order(iterable): 
    item = None 
    list_in_order = [] 
    for i in iterable: 
        if i != item: 
            list_in_order.append(i) 
            item = i 
    return list_in_order

iterable1 = 'AAAABBBCCDAABBB'
iterable2 = 'ABBCcAD'
iterable3 = [1,2,2,3,3]

print(iterable1)
print(unique_in_order(iterable1))
print(iterable2)
print(unique_in_order(iterable2))
print(iterable3)
print(unique_in_order(iterable3))