#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:45:28 2021

@author: rajkumarpal
Problem : Day 5 - Normal Distribution II

---Task---
The final grades for a Physics exam taken by a large group of students have a 
mean of mi = 70 and a standard deviation of sigma = 10. If we can approximate 
the distribution of these grades by a normal distribution, 
what percentage of the students:
1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a grade < 60)?
"""


# erf --> import error function
from math import erf

def cumulative_prob(x, mean, std):
    function = 0.5 * ( 1 + erf((x - mean) / (std*(2**0.5))))
    return function

x = list(map(float, input().split()))
mean = x[0] 
std = x[1]
sc1 = float(input())
sc2 = float(input())

#Scored higher than 80
print(round(100 - cumulative_prob(sc1, mean, std)*100, 2))
#Passed the test (grade>=60)
print(round(100 - cumulative_prob(sc2, mean, std)*100, 2))
#Failed the test (grade<60)
print(round(cumulative_prob(sc2, mean, std)*100, 2))