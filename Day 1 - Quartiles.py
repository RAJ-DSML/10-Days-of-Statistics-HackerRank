#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:59:34 2021

@author: rajkumarpal
Problem Name: Day 1 : Quartiles
"""
n = int(input().strip())
array = sorted(list(map(int,input().split())))

def median_value(n, value):
    if n%2 == 0:
        mid = (value[int(n/2)-1] + value[int(n/2)]) / 2
    else:
        mid = value[int(n/2)]
    return int(mid)

if n%2 == 0:
    Q1 = array[0:int(n/2)]
    Q3 = array[int(n/2):n]
else:
    Q1 = array[0:int(n/2)]
    Q3 = array[int(n/2)+1:n]
    
print(median_value(len(Q1), Q1))
print(median_value(n, array))
print(median_value(len(Q3), Q3))