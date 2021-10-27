#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:52:36 2021

@author: rajkumarpal
Problem Name: Day 0: Mean, Median, and Mode
"""

import numpy as np
from scipy import stats

N = int(input())
X = list(map(int, input().split()))

print(np.mean(X))
print(np.median(X))
print(int(stats.mode(X)[0]))