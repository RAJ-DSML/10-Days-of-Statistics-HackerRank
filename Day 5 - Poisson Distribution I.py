#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:13:22 2021

@author: rajkumarpal
Problem: Day 5 - Poisson Distribution I

---Task---
A random variable, X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.
"""


# factorial function
def factorial(n):
    if n == 0:
        return 1 
    else:
        return n*factorial(n-1)
    
    
lambdaa = float(input())
k = float(input())
e = 2.718

poisson = (lambdaa**k * e**(-lambdaa))/factorial(k) 
print(round(poisson, 3))