# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:38:35 2017

@author: rubadani
"""

x = [1.123456789*10e10, 1.123456789*10e14, 1.123456789*10e15, 1.123456789*10e16,1.123456789*10e20]
for i in range (0, 5):
    result1 = x[i] + 0.1 - x[i]
    result2 = x[i] - x[i] + 0.1
    print(result1, result2)
