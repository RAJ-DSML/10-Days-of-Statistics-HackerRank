#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:17:59 2021

@author: rajkumarpal
Problem: Day 5 - Poisson Distribution II
---Task---
The manager of a industrial plant is planning to buy a machine of either type A or type B. 
For each day’s operation:

>The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
The daily cost of operating A is CA = 160 + 40X^2.

>The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
The daily cost of operating B is CB = 180 + 40Y^2.

Assume that the repairs take a negligible amount of time and 
the machines are maintained nightly to ensure that they operate 
like new at the start of each day. Find and print the expected daily cost for each machine.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
lambdaa = list(map(float, input().split()))
Ca = lambdaa[0]
Cb = lambdaa[1]

print (round(160 + 40 * (Ca + Ca ** 2), 3))
print (round(128 + 40 * (Cb + Cb ** 2), 3))