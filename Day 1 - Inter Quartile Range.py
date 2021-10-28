#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:22:11 2021

@author: rajkumarpal
Problem Name: Day 1 : Inter Quartile Range
"""

n = int(input().strip())
val = list(map(int, input().rstrip().split()))
freq = list(map(int, input().rstrip().split()))

def median_value(n, value):
    if n%2 == 0:
        mid = (value[int(n/2)-1]+value[int(n/2)])/2
    else:
        mid = float(value[int(n/2)])
    return mid

S = []
for i in range(len(val)):
    for j in range(freq[i]):
        S.append(val[i])
S = sorted(S)
    
n = len(S)
if n%2 == 0:
    Q1_s = S[0:int(n/2)]
    Q3_s = S[int(n/2):n]
else:
    Q1_s = S[0:int(n/2)]
    Q3_s = S[int(n/2)+1:n]    

Q1 = median_value(len(Q1_s), Q1_s)
Q3 = median_value(len(Q3_s), Q3_s)    
print(Q3-Q1)