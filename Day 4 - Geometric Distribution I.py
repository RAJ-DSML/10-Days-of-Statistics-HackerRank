#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:59:07 2021

@author: rajkumarpal
Problem: Day 4 - Geometric Distribution I
"""


inputs = list(map(int, input().split()))
p = inputs[0]/inputs[1]
q = 1 - p
n = int(input())

# geometric distribution function
g_dist = q ** (n-1) * p
print(round(g_dist, 3))