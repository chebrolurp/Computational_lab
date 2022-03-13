import math
import random
import numpy  as np


def nthroot(n,a,e):
    error  = np.inf
    x0  =  random.randint(1,9)
    while(error > e):
        x = ((n-1)*x0 + a/pow(x0,n-1))/n
        error =  abs(x-x0)
        x0 = x
    return x0
 
if __name__ =="__main__":
   #print(nthroot(10,4,0.0001))
