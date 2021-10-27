#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:56:08 2021

@author: rajkumarpal
Problem Name: Day 0 : Weighted Mean
"""


n = int(input())
vals = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))
r = 0

for i in range(n):
    r =  r + (vals[i]*weights[i])
    
print(round(r/sum(weights), 1))