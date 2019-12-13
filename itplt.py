#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:21:15 2019

@author: chintan
"""
from numpy import array,arange
from scipy.interpolate import lagrange,InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
x=array([0,1,2,3,4,5])
y=array([1,2,1,.5,4,8])
ylin=InterpolatedUnivariateSpline(x,y,k=1)
yq=InterpolatedUnivariateSpline(x,y,k=2)
yc=InterpolatedUnivariateSpline(x,y,k=3)
yl=lagrange(x,y)
xfit=arange(0,5.5,.01)
plt.plot(xfit,ylin(xfit),label='linear')
plt.plot(xfit,yq(xfit),label='quadratic')
plt.plot(xfit,yc(xfit),label='cubic')
plt.plot(xfit,yl(xfit),label='lagrange') 
plt.scatter(x,y,label='data')
plt.legend()
plt.title('Example')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

