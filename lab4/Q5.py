import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.integrate import simps

def func(x):
    return 2*x*np.exp(x**2)
def visualize():
    U = np.linspace(1,20,10,dtype='int')
    AA = []
    qA = []
    TA = []
    SA = []
    for u in U:
        area,_ = integrate.quad(func,0,u)
        qA.append(area)
        AA.append(np.exp(u**2)-np.exp(0))
        X = np.linspace(0,u,20)
        TA.append(integrate.trapezoid(2*X*np.exp(X**2),X))
        SA.append(simps(2*X*np.exp(X**2),X))
    plt.plot(U,AA,c='g',marker='o',label='True Area')
    plt.plot(U,qA,c='r',marker='+',label = "quad")
    plt.plot(U,TA,c='b',marker='.',label = "Trapezoid")
    plt.plot(U,TA,c='k',label = "simps")
    plt.legend()
    plt.xlabel('m')
    plt.yscale("log")
    plt.ylabel('log Area')
    plt.show()
if __name__ =="__main__":
    pass
    #visualize()
