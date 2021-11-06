#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:59:10 2021

@author: rajkumarpal
Problem: Day 8 - Least Square Regression Line
"""


import statistics as st

n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

mu_x = st.mean(x)
mu_y = st.mean(y)
x_sq = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

b = (n * xy - sum(x) * sum(y)) / (n * x_sq - (sum(x) ** 2))
a = mu_y - b * mu_x

print (round(a + 80 * b, 3))