#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:23:38 2021

@author: rajkumarpal
Problem: Day 5 - Normal Distribution I

 ---Task---
In a certain plant, the time taken to assemble a car is a random variable, X, 
having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. 
What is the probability that a car can be assembled at this plant in:
    
1. Less than 19.5 hours?
2. Between 20 and 22 hours?
"""

# erf --> import error function
from math import erf

def cumulative_prob(x, mean, std):
    function = 0.5 * ( 1 + erf((x - mean) / (std*(2**0.5))))
    return function

x = list(map(float, input().split()))
mean = x[0] 
std = x[1]
less = float(input())
between = list(map(float, input().split()))

#less than 19.5 hours
print(round(cumulative_prob(less, mean, std),3))
#between 20 and 22 hours
print(round(cumulative_prob(between[1], mean, std) - cumulative_prob(between[0], mean, std),3))