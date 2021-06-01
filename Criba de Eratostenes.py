# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:22:58 2020

@author: David
"""
	
n=33
for ainv in range(14220,14225):
    for j in range (1,pow(n,3)+1):
        if (j*ainv)%pow(n,3)==1:
            print ((j*ainv)%pow(n,3), ainv, j)