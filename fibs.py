#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW02 Exercise 2



def fibs(n):
    numbers=[1,1]
    k=1
    while (k+1)<n:
        numbers.append(numbers[k-1]+numbers[k])
        k+=1
    return numbers

def fib_generator():
    a = 0
    b = 1
    c = 1
    while True:
        yield c
        c = a + b
        a=b
        b=c

if __name__ in =="__main__":
    n=input("value for n:")
    print (fibs(n))
    g = fib_generator()
    [next(g) for _ in range(5)]




