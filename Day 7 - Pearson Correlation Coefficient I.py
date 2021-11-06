#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:52:30 2021

@author: rajkumarpal
Problem: Day 7 - Pearson Correlation Coefficient I
"""

import statistics as st
def pearson_correlation_coefficient(n, xi, yi):
    mu_x = st.mean(xi)
    mu_y = st.mean(yi)
    sigma_x = st.pstdev(xi)
    sigma_y = st.pstdev(yi)
    pxy = 0
    for i in range(n):
        pxy += (xi[i] - mu_x) * (yi[i] - mu_y)
    return pxy/(n * sigma_x * sigma_y)

n = int(float(input()))
xi = list(map(float, input().split()))
yi = list(map(float, input().split()))

print(round(pearson_correlation_coefficient(n, xi, yi),3))