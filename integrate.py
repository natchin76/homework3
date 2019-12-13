#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:58:07 2019

@author: chintan
"""
from numpy import exp
from numpy import arange
from numpy import trapz
from scipy.integrate import simps,romberg,fixed_quad
x=arange(0,1,1e-5)
y=exp(x)
I_trp=trapz(y,x)
I_simps=simps(y,x)
def f(a):
    return(exp(a))
I_rom=romberg(f,0,1)
I_gauss=fixed_quad(f,0,1,n=5)

