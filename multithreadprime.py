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

if __name__ == "__main__":
    num_iter = 20
    t = timeit.timeit("prime_list_test(10**6)",setup='from multithreadprime import prime_list_test',number=num_iter)
    #l = prime_list_test(10**6)
    print(t/num_iter)