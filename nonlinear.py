#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:33:09 2019

@author: chintan
"""
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import bisect as bis
def f(x):
    return(np.sin(np.cos(np.exp(x))))
root=bis(f,-1,1) 
x=np.arange(-1,1,.01)
y=f(x)
plt.plot(x,y)
print(root,f(root))   