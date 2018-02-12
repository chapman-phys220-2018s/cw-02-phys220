#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compute_sum(tol = 1e-2):
    k=1
    sum_total = 0
    sum_term = 1
    while sum_term > tol:
        sum_term = 1/(k**2)
        sum_total += sum_term
        k += 1
    return sum_total


