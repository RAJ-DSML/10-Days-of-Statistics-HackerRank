#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:54:36 2021

@author: rajkumarpal
Problem: Day 4 - Binomial Distribution II
---Task---
A manufacturer of metal pistons finds that, on average, 
12% of the pistons they manufacture are rejected because they are incorrectly sized. 
What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?
"""


# factorial function
def factorial(n):
    if n == 0:
        return 1 
    else:
        return n*factorial(n-1)

inputs = list(map(float, input().split()))
p = (inputs[0] / 100)
n = int(inputs[1])

def binomial_func(x, n, p):
    q = 1.0 - p
    bernoulli_equ = p**x * q ** (n-x)
    combination = factorial(n) / (factorial(x) * factorial(n-x))
    return combination * bernoulli_equ

# No more than 2 rejects
no_more_than_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_than_2_rejects +=  binomial_func(i, n, p)
print(round(no_more_than_2_rejects, 3))

# At least 2 rejects
at_least_2_rejects = 0
for i in range(n):
    if i > 1:
        at_least_2_rejects += binomial_func(i, n, p)
print(round(at_least_2_rejects, 3))