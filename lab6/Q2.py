import math
import matplotlib.pyplot as plt
import numpy as np

def Exact_Solution(t):
    x = 5*math.exp(-2*t)
    return x

def Backword_Eular_Method():
    H = [0.1, 0.5, 1, 2, 3]
    for h in H:
        X = []
        T = []
        x0 = 5
        t = 0
        while t < 10:
            X.append(x0)
            T.append(t)
            t += h
            
            x0 = x0/(1+2*h) 
            
        plt.plot(T,X,label = 'step size = {}'.format(h),marker = '.')
        
    T = np.linspace(0,10,100)
    X = [Exact_Solution(t) for t in T]
    plt.plot(T,X, label = 'Exact Solution')
    plt.xlabel('time')
    plt.ylabel('x')
    plt.legend()
    plt.title('Backword Euler Method')
    plt.show()
    
if __name__=="__main__":
    
    Backword_Eular_Method()
    pass
