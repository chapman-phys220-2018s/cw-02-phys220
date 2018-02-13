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


#def compute_sumlarge(tol=1e-20):
    #sum=0
    #k=float(1)
    #if tol<(1/(k**2))
        #sumlarge += (1/(k**2))
        #k +=1
    #return sum
#We can do this by replacing tol with any number we want in jupyter

<<<<<<< HEAD
if __name__ in "__main__":
    print ("If tol=1e-2, then it converges at "compute_sum)
    print ("If tol=1e-20, then it converges at " compute_sumlarge)
    
=======
#if __name__ in "__main__":
    #print ("If tol=1e-2, then it converges at "compute_sum)
    #print ("If tol=1e-20, then it converges at" compute_sumlarge)
>>>>>>> d010be1caa6255591411bd49544312b8ca008679

    #We don't need this if we are calling the functions into our jupyter notebook, so we can remove it
    #if we want less clutter


