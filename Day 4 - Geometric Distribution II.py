#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 00:03:12 2021

@author: rajkumarpal
Problem: Day 4 - Geometric Distribution II

---Task---
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the first 5 inspections?
"""


inputs = list(map(int, input().split()))
p = inputs[0]/inputs[1]
q = 1 - p
n = int(input())

# geometric distribution function for 1st defect found during the first 5 inspections
g_dist = 0
for i in range(n+1):
    if i > 0:
        g_dist += q ** (i-1) * p
print(round(g_dist, 3))