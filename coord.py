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
    a=float(a)
    b=float(b)
    coords = []
    inc = (b-a)/ n
    for x in range(n+1):
        coords.append(a+inc*x)
    return coords


def coord_while(n, a=0, b=1):
    a=float(a)
    b=float(b)
    coords=[]
    num=a
    while num!=(n+1):
        coords.append((b-a)*num/n)
        num=len(coords)
    return coords
<<<<<<< HEAD

def coords_comp(n, a=0, b=1):
    coords=[(b-a)*k/n for k in range(n+1)]
    return coords
=======
    

if __name__ == "__main__":
    print("choose values for n, a, and b.")
    n_int= int(input ("number of intervals n+1:"))
    a_int= int(input ("starting value =a:"))
    b_int= int(input ("last value =b:"))
    for_list= (coord_for(n,a,b))
    while_list=coord_while(n,a,b)
    print(str(for_list))
    print(str(while_list))
    
>>>>>>> 327d56c5d112ab9034652fae09982f4635358dca
