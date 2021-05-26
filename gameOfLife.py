import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
import math
import scipy.fft as fft
from functools import partial
from scipy import signal

def computeStep(inp):
    kernel = np.ones((3, 3), dtype=int)
    kernel[1, 1] = 0
    def cellLife(n, cell):
        if cell == 1:
            if n <=1:
                return 0
            if n>=4:
                return 0
            if (n==2 or n==3):
                return 1
        else:
            if n == 3:
                return 1
            else:
                return 0
            
    def cellLifeRow(n, cell):
        return list(map(cellLife, n, cell))
    
    counter = signal.convolve(inp, kernel, mode='same')
    n_step = map(cellLifeRow, counter, inp)
    #print(np.array(list(n_step)))

    return np.array(list(n_step))

def computeIterations(inp, iters):
    s = inp.shape
    res = np.zeros(s[0]*s[1]*iters, dtype = int).reshape(iters, s[0], s[1])
    res[0] = np.copy(inp)
    
    for i in range(1, iters):
        res[i] = computeStep(res[i-1])
        
    return res