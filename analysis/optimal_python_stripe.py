#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:44:20 2023

@author: akswart
"""

import sys
import numpy as np
sys.path.insert(0, "../python/")
from multithreadprime import multiprime

def generate_data(start_power,end_power,power_step,
                  start_stripe,end_stripe, num_iter = 10):

    for p in np.arange(start_power,end_power+power_step,power_step):
        for stripe in range(start_stripe,end_stripe+1):
            t_avg = multiprime(p,num_iter,stripe)
            print("Running with pow:{}, stripe:{}, time: {}".format(p,stripe,t_avg))
            
if __name__ == "__main__":    
    generate_data(5, 8, .25, 1, 8)