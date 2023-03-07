#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:28:05 2023

@author: akswart
"""
import math
import numpy as np
import timeit

def is_prime(test_num):
    # Tests if k is prime
    if test_num == 2:
        return True
    for test_div in range(2,math.ceil(np.sqrt(test_num))+1):
        if test_num % test_div == 0:
            return False
    return True

def prime_list(my_list):
    return [p for p in my_list if is_prime(p)]

def non_parallel_primes(end_power):
    nump = 0
    for i in np.arange(1,end_power,dtype=np.int64):
        ap = 10**(i-1)
        bp = 10**i
        p = prime_list(range(ap,bp))
        nump += len(p)
    return nump 