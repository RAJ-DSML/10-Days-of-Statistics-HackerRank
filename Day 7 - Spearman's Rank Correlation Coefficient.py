#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:55:25 2021

@author: rajkumarpal
Problem: Day 7 - Spearman's Rank Correlation Coefficient
"""


def rank_fun(dt):
    rank = {}
    sorted_rank = sorted(dt)
    for i in range(len(dt)):
        for j in range(len(sorted_rank)):
            if dt[i] == sorted_rank[j]:
                rank[dt[i]] = j+1
    return rank

def spearmans_rank_corr_coeff(x, y, n, r_x, r_y):
    rs = 0
    for i in range(n):
        if r_x[x[i]] != r_y[y[i]]:
            rs += ((r_x[x[i]] - r_y[y[i]]) ** 2)
    return (6 * rs) / (n * (n**2 - 1))


n = int(float(input()))
data_x = list(map(float, input().split()))
data_y = list(map(float, input().split()))
r_x = rank_fun(data_x)
r_y = rank_fun(data_y)

# Gets the result and show on the screen
Rxy = spearmans_rank_corr_coeff(data_x, data_y, n, r_x, r_y)
print(round(1 - Rxy, 3))