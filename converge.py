#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#Devon Ball
#2313078
#dball#chapman.edu
#PHYS220 Spring 2018
#CW02 Exercise 3

def compute_sum(tol = 1e-2):
    """Function computes the sum of 1/k**2.
    tol represents a specific tolerance.
    Summation is to stop when the sum would be smaller than the specified tolerance."""
    k=1
    sum_total = 0
    sum_term = 1
    while sum_term > tol:
        sum_term = 1/(k**2)
        sum_total += sum_term
        k += 1
    return sum_total


