#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:29:33 2021

@author: rajkumarpal
Problem: Day 6 - The Central Limit Theorem II

---Task---
The number of tickets purchased by each student for the University X vs. University Y 
football game follows a distribution that has a mean of u = 2.4 and
a standard deviation of 20. A few hours before the game starts, 100 eager students 
line up to purchase last-minute tickets. If there are only 250 tickets left, what is the
probability that all 100 students will be able to purchase tickets?

"""


from math import erf, sqrt

def cumulative(value, mean, std):
    return 0.5 * (1 + erf((value - mean) / (std * (2 ** 0.5))))

max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

mean2 = mean * n
std2 = sqrt(n) * std

print (round(cumulative(max_weight, mean2, std2),4))