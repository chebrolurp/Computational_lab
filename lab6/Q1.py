import math
import matplotlib.pyplot as plt
import numpy as npy 

def Exact_Solution(t):
    x = 5*math.exp(-2*t)
    return x

def Forward_Eular_method():
    H = [0.1, 0.5, 1, 2, 3]
    t0 = 0
    T = 10
    t = t0
    x0 = 5
    for h in H:
        X = []
        T = []
        x0 = 5
        t = 0
        while t < 10:
            X.append(x0)
            T.append(t)
            t += h
            x0 = x0 - h*2*x0
            
        plt.plot(T,X,label = 'step size = {}'.format(h),marker = '.')
        
    T = np.linspace(0,10,100)
    X = [Exact_Solution(t) for t in T]
    plt.plot(T,X, label = 'Exact Solution')
    plt.xlabel('time')
    plt.ylabel('x')
    plt.legend()
    plt.title('Forward Euler Method')
    plt.show()
    
if __name__ =="__main__":
    
    #Forward_Eular_method()
    pass
