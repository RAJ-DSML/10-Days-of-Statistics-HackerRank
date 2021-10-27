# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Raj Kumar Pal
File Name: Day 0: Mean, Median, and Mode
"""

import numpy as np
from scipy import stats

N = int(input())
X = list(map(int, input().split()))

print(np.mean(X))
print(np.median(X))
print(int(stats.mode(X)[0]))