#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:28:05 2023

@author: akswart
"""
import math
import numpy as np
import time
import os
import csv

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

def singleprime(end_power,num_iter,debug = False):
    t = []
    for i in range(num_iter):
        t0 = time.time()
        non_parallel_primes(end_power)
        t1 = time.time()
        t.append(t1-t0)
        if debug:
            print("Done: ",t1-t0)
        
    t_avg = sum(t)/len(t)
    outlist = ["Python",str(end_power),str(num_iter),str(t_avg)]
    
    # If the output does not exist, then create a csv file with column headers
    filepath = "../data/singleresults.csv"
    if not os.path.exists(filepath):
        with open(filepath,'w',newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Language","End Power","Num Iter", "Average"])
   
    # Write results with config data
    with open(filepath,'a',newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(outlist)
        
    return t_avg

if __name__ == "__main__":
    power_step = .25
    end_power = 6
    for p in np.arange(1,end_power+power_step,power_step):
        t_avg = singleprime(p, 5)
    # Get a baseline for single threaded performance
    