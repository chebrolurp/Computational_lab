import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate

def Fourier_approx(x,A,B,a0,n):
        val = a0
        for i in range(1,n+1):
            val+= A[i-1]*math.cos(i*x) + B[i-1]*math.sin(i*x)
        return val
    
def FourierApprox(n):
    A = []
    B = []
    a0,_= integrate.quad(lambda x: math.exp(x),-math.pi,math.pi)
    a0 = a0/(2*math.pi)
    for i in range(1,n+1):
        a,_ = integrate.quad(lambda x: math.exp(x)*math.cos(i*x),-math.pi,math.pi)
        A.append(a/math.pi)
        b,_ = integrate.quad(lambda x: math.exp(x)*math.sin(i*x),-math.pi,math.pi)
        B.append(b/math.pi)
        
    print("a0 = ",a0*2)
    print("\n")
    print("A", A)
    print("\n")
    print("B" , B)
    
    X = np.linspace(-math.pi,math.pi,50)
    Y = np.exp(X) 
    Y_approx = [Fourier_approx(x,A,B,a0,n) for x in X]
    plt.scatter(X,Y,marker ='+',color = 'r',label = 'exp(x)')
    plt.plot(X,Y_approx,label = 'FourierApprox')
    plt.title("{} order Fourier approximation of exp(x)".format(n))
    plt.legend()
    plt.show()
    
if __name__=="__main__":
    #FourierApprox(10)
    pass
