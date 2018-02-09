#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module Description:
Module contains function coord_for(n, a=0, b=0) that takes a number of intervals and two
end points of a segment and returns a list of the interval division coordinates.

Arguments:
n - the number of intervals
a - lower segment bound that has been given a default value of a=0
b - upper segment bound that has been given a default value of b=0
"""
def coord_for(n, a=0, b=1):
    coords = []
    inc = (b-a)/ n
    for x in range(n+1):
        coords.append(a+inc*x)
    return coords

def coord_while(n, a=0, b=1):
    coords=[]
    k=len(coords)
    while k<(n+1):
        k=len(coords)
        coords.append((b-a)*k/n)
    return coords

