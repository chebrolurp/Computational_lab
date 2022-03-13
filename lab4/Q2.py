import numpy as np
import matplotlib.pyplot as plt

def visualize():
    X = np.linspace(0,1,100)

    # function derivative
    fx = np.cos(X**2)*2*X

    h = 0.01

    #Forward finite difference error
    efx1 = np.abs(fx - np.array([(np.sin((x+h)**2) - np.sin(x**2))/h for x in X]))

    #Backword finite difference error
    efx2 = np.abs(fx - np.array([(-np.sin((x-h)**2) + np.sin(x**2))/h for x in X]))

    #Centered finite difference error
    efx3 = np.abs(fx - np.array([(np.sin((x+0.01)**2) - np.sin((x-0.01)**2))/(2*h) for x in X]))


    #plt.plot(X,fx,c='g',marker= '+',label = 'True')
    plt.plot(X,efx1,c='b',marker = '',label = 'forward')
    plt.plot(X,efx2,c='r',marker = '.',label = 'backword')
    plt.plot(X,efx3,c='k',label = 'Centered')
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Absolute errors for finite differences')
    plt.legend()
    plt.show()
    
if __name__=="__main__":
    #visualize()
