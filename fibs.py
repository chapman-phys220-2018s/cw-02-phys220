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
#dball@chapman.edu
#PHYS220 Spring 2018
#CW02 Exercise 2



def fibs(n):
    """Function takes a positive integer, n, and returns a list of Fibonacci numbers."""
    numbers=[1,1]
    k=1
    while (k+1)<n:
        numbers.append(numbers[k-1]+numbers[k])
        k+=1
    return numbers

def fib_generator():
    """Function creates a list of Fibonacci numbers starting at 1."""
    a = 0
    b = 1
    c = 1
    while True:
        yield c
        c = a + b
        a=b
        b=c





