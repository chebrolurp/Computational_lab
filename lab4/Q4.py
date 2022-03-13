import numpy as np
import matplotlib.pyplot as plt

def visualize():
    # Actual Area
    Area = (np.exp(9)-np.exp(1))
    
    M = np.linspace(100,1000,100,dtype=int)
    TA = []
    for m in M:
        X = np.linspace(1,3,m)
        f = 2*X*np.exp(X**2)
        
        # Trapezoid Formulae
        A = (f[0]+f[-1]+ 2*sum(f[1:-1]))/m
        TA.append(A)
        
    plt.plot(M,TA,c='r',label = "Trapezoid")
    plt.axhline(y = Area,c='g',label='True Area')
    plt.legend()
    plt.xlabel('m')
    plt.ylabel('Area')
    plt.show()

if __name__=="__main__":
    pass
    #visualize()
