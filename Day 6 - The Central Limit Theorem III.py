#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:34:59 2021

@author: rajkumarpal
Problem: Day 6 - The Central Limit Theorem III

---Task---
You have a sample of 100 values from a population with mean u = 500 and with 
standard deviation a = 80. Compute the interval that covers the middle 95% of 
the distribution of the sample mean; in other words, compute A and B such that 
P(A < x < B) = 0.95. Use the value of z = 1.96. Note that z is the z-score.
"""


from math import sqrt

n = float(input())
mean = float(input())
std = float(input())
p = float(input())
z_value = float(input())

clt = z_value * (std/sqrt(n))

print(round(mean-clt,4))
print(round(mean+clt,4))