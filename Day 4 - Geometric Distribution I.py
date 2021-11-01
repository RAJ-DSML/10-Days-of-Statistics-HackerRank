#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:59:07 2021

@author: rajkumarpal
Problem: Day 4 - Geometric Distribution I

---Task---
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect occurs the 5th item produced?
"""


inputs = list(map(int, input().split()))
p = inputs[0]/inputs[1]
q = 1 - p
n = int(input())

# geometric distribution function
g_dist = q ** (n-1) * p
print(round(g_dist, 3))