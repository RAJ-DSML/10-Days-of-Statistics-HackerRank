#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:26:10 2021

@author: rajkumarpal
Problem: Day 4 - Binomial Distribution 1

---Task---
The ratio of boys to girls for babies born in Russia is 1.09:1. 
If there is 1 child born per birth, what proportion of Russian families with exactly  
6 children will have at least 3 boys?

"""

# factorial function
def factorial(n):
    if n == 0:
        return 1 
    else:
        return n*factorial(n-1)

#combnination function   
def combination(n, x):
    result = factorial(n) / (factorial(x) * factorial(n-x))
    return result

#binomial distribution function
def binom(x, n, p):
    return combination(n, x) * p**x *(1-p)**(n-x)

l_value, r_value = list(map(float, input().split()))
odds = l_value / r_value
print(round(sum([binom(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))