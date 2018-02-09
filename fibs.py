#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibs(n):
    numbers=[1,1]
    k=1
    while (k+1)<n:
        numbers.append(numbers[k-1]+numbers[k])
        k+=1
    return numbers