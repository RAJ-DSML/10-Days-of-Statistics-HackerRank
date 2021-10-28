#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:28:03 2021

@author: rajkumarpal
Problem Name: Day 1 : Standard Deviation
"""

import math

def mean(value):
    return sum(value)/len(value)

def stdDev(value, n):
    # Print your answers to 1 decimal place within this function
    result = 0
    for i in range(n):
      result += (value[i] - mean(value)) ** 2   
    return math.sqrt(result/n)

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))

    print(round(stdDev(vals, n),1))