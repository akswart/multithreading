#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:55:45 2020

@author: aswart
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

def prime_list_test(n):
    prime_list = [2]
    prime_list_nums = 1
    #print(is_prime(prime))
    prime = 3
    while prime <= n:
        if is_prime(prime):
            #prime_list.append(prime)
            prime_list_nums += 1
        prime += 2
    #return len(prime_list)
    return prime_list_nums

def prime_list(my_list):
    """
    a = []
    for p in my_list:
        #print(p)
        if is_prime(p):
            a.append(p)
            
    return a
    """
    return [p for p in my_list if is_prime(p)]

import multiprocessing

def parallel_primes(end_power):
    primes = np.arange(1,end_power,dtype=np.int64)
    prime_range = [range(10**(i-1),10**i) for i in primes]
    p = multiprocessing.Pool()    
    result = p.map(prime_list,prime_range)
    a = sum([len(i) for i in result])
    #lens = p.map(len,result)
    #a = sum(lens)
    return a

def non_parallel_primes(end_power):
    nump = 0
    for i in np.arange(1,end_power,dtype=np.int64):
        a = 1
        b = 100
        ap = 10**(i-1)
        bp = 10**i
        p = prime_list(range(ap,bp))
        nump += len(p)
    return nump 

if __name__ == "__main__":    

    end_power = 7
    num_iter = 10
    
    # Check equality
    #print(parallel_primes(end_power) == non_parallel_primes(end_power))
    
    #run1 = "non_parallel_primes({})".format(end_power)
    run2 = "parallel_primes({})".format(end_power)
    #tn = timeit.timeit(run1,setup='from multithreadprime_2 import non_parallel_primes',number=num_iter)
    #print("Non-para",tn/num_iter)
    tp = timeit.timeit(run2,setup='from multithreadprime_2 import parallel_primes',number=num_iter)
    print("Para",tp/num_iter)
    
    '''
    times = []
    base = []
    nump = 0
    for i in np.arange(1,10,dtype=np.int64):
        a = 1
        b = 100
        ap = 10**i
        bp = 10**i+500
        p = prime_list(range(ap,bp))
        nump += len(p)
        #run = "prime_list(range("+str(ap)+","+str(bp)+"))"
        #t = timeit.timeit(run,setup='from multithreadprime_1 import prime_list',number=num_iter)
        
        """
        if times:
            times.append((t/num_iter)/times[0])
        else:
            times.append(t/num_iter)
        base.append(ap)
        """
    
    """
    times[0] = 1
    print(times)
    print(base)
    import matplotlib.pyplot as plt
    plt.semilogx(base,times)
    plt.loglog(base,times)
    """
    #l = prime_list_test(10**6)
    #print(t/num_iter)
    
    
    '''