#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def coord_for(n, a=0, b=1):
    coords = []
    int_l = b-a
    inc = int_l / n
    for x in range(n+1):
        coords.append(a+inc*x)
    return coords
