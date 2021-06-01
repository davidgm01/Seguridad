#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:50:33 2020

@author: Lion
"""

import os
n=33
for ainv in range(17986,18001):
    for j in range (1,pow(n,3)+1):
        if (j*ainv)%pow(n,3)==1:
            for b in range(27001,27051):
                if os.path.exists("Archivo desencriptado {} - {}.txt".format(ainv,b)):
                    os.remove("Archivo desencriptado {} - {}.txt".format(ainv,b))
print('Archivos eliminados')