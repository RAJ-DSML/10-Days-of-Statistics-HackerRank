#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:52:59 2021

@author: rajkumarpal
Problem: Day 6 - Central Limit Theorem I

---Task---
A large elevator can transport a maximum of 9800 pounds. 
Suppose a load of cargo containing 49 boxes must be transported via the elevator.
The box weight of this  type of cargo follows a distribution with a mean of u = 205 pounds 
and a standard deviation of a = 15 pounds. Based on this information, what is the
probability that all 49 boxes can be safely loaded into the freight elevator and transported?
"""

from math import erf, sqrt

def cumulative_prob(value, mean, std):
    function = 0.5 * ( 1 + erf((value - mean) / (std*(2**0.5))))
    return function

max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())
mean2 = mean * n
std2 = sqrt(n) * std

#Print the prob. that the elevator can successfully transport all 49 boxes
print(round(cumulative_prob(max_weight, mean2, std2), 4))