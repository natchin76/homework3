#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:48:03 2019

@author: chintan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:33:09 2019

@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
from numpy import sin,cos,exp
from scipy.optimize import newton
def f(x):
    return(np.sin(np.cos(np.exp(x))))   
root=newton(f,-.1)        
print('guess value:-0.1',root,f(root))
root=newton(f,-1)
print('guess value:-1',root,f(root))
   
