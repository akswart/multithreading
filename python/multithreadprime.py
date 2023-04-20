#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:55:45 2020

@author: aswart
"""
import math
import numpy as np
import multiprocessing
import csv
import sys
import os.path
import time

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


def parallel_primes(end_power,stripe_power):
    stripe_size = 10**stripe_power
    total_size = 10**end_power
    # build prime interval array
    prime_range = [range(1+i*stripe_size,1+(i+1)*int(min(stripe_size,total_size))) 
                   for i in range(0,int(total_size/min(stripe_size,total_size)))]
    # The min is for the rare case where the stripe_size > total_size

    p = multiprocessing.Pool()    
    result = p.map(prime_list,prime_range)
    a = sum([len(i) for i in result])

    p.close()
    p.join()
    return a


def multiprime(end_power,num_iter,stripe_power,debug = False):
    t = []
    for i in range(num_iter):
        t0 = time.time()
        parallel_primes(end_power,stripe_power)
        t1 = time.time()
        t.append(t1-t0)
        if debug:
            print("Done: ",t1-t0)
        
    t_avg = sum(t)/len(t)
    outlist = ["Python",str(end_power),str(stripe_power),str(num_iter),str(t_avg)]
    
    # If the output does not exist, then create a csv file with column headers
    filepath = "../data/multiresults.csv"
    if not os.path.exists(filepath):
        with open(filepath,'w',newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Language","End Power","Stripe Power","Num Iter", "Average"])
   
    # Write results with config data
    with open(filepath,'a',newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(outlist)
        
    return t_avg



if __name__ == "__main__":    

   # Default Values
    end_power = 8
    num_iter = 10
    stripe_power = 4
    
    if len(sys.argv) == 2:
        end_power = float(sys.argv[1])
    elif len(sys.argv) == 3:
        end_power = float(sys.argv[1])
        num_iter = int(sys.argv[2])
    elif len(sys.argv) == 4:
        end_power = float(sys.argv[1])
        num_iter = int(sys.argv[2])
        stripe_power = int(sys.argv[3])
    else:
        print("Incorrect/No command line arguments given, using default vals")


    t_avg = multiprime(end_power,num_iter,stripe_power)
    print("Average time: ",t_avg)

    
    
