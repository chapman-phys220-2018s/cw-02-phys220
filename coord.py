#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#PHYS220 Spring 2018
#CW02 Exercise 1

"""
Arguments:
n - the number of intervals
a - lower segment bound that has been given a default value of a=0
b - upper segment bound that has been given a default value of b=0
"""

def coord_for(n, a=0, b=1):
    """Function that takes 3 parameters or arguments, listed above, and returns a list of the interval division             coordinates."""
    a=float(a)
    b=float(b)
    coords = []
    inc = (b-a)/ n
    for x in range(n+1):
        coords.append(a+inc*x)
    return coords


def coord_while(n, a=0, b=1):
    """Function does the same thing as coord_for but uses a while loop instead of for."""
    a=float(a)
    b=float(b)
    coords=[]
    num=a
    while num!=(n+1):
        coords.append((b-a)*num/n)
        num=len(coords)
    return coords

def coord_comp(n, a=0, b=1):
    """Function also does the same but uses a list comprehension instead of loops. """
    coords=[(b-a)*k/n for k in range(n+1)]
    return coords

