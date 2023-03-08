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
    if test_num % 2 == 0:
        return False
    for test_div in range(3,math.ceil(np.sqrt(test_num))+1,2):
        if test_num % test_div == 0:
            return False
    return True

# Simplest possible Sieve of Eratosthenes
def is_prime_simple(test_num):
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
    for i in np.arange(1,end_power+1,dtype=np.int64):
        ap = 10**(i-1)
        bp = 10**i
        p = prime_list(range(ap,bp))
        nump += len(p)
    return nump
 
def test1(end_power):
    nump = len(prime_list(range(1,int(10**end_power))))
    return nump

def test2(end_power):
    nump = 0
    for i in range(1,int(10**end_power)):
        if is_prime(i):
            nump += 1
    return nump

def benchmark1(end_power,num_iter):
    t = []
    for i in range(num_iter):
        t0 = time.time()
        n = test1(end_power)
        t1 = time.time()
        t.append(t1-t0)
    #print("New:",n)
    return sum(t)/len(t)

def benchmark2(end_power,num_iter):
    t = []
    for i in range(num_iter):
        t0 = time.time()
        n = test2(end_power)
        t1 = time.time()
        t.append(t1-t0)
    #print("New:",n)
    return sum(t)/len(t)

def singleprime(end_power,num_iter,debug = False):
    t = []
    for i in range(num_iter):
        t0 = time.time()
        n = non_parallel_primes(end_power)
        t1 = time.time()
        t.append(t1-t0)
        if debug:
            print("Done: ",t1-t0)
    #print("Old:",n)
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
    num_iter = 10
    score = 0
    for p in np.arange(5,8,.25):
        t_avg1 = benchmark1(p, num_iter)
        t_avg2 = benchmark2(p, num_iter)
        
        print("p = {}: Method1 {:5f}, Method2 {:5f}".format(p,t_avg1,t_avg2))
        #t_avgold = singleprime(p, num_iter)
        #print("p = {:d}: Method1 {:5f}, Old Method {:5f}".format(p,t_avg1,t_avgold))
        #if t_avg1 <= t_avgold:
        #    score += 1
              
    """
    power_step = .1
    end_power = 7
    for p in np.arange(1,end_power+power_step,power_step):
        t_avg = singleprime(p, 5)
        print("Running with pow:{}, time: {}".format(p,t_avg))
    # Get a baseline for single threaded performance
    """