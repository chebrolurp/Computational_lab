import numpy as np
import matplotlib.pyplot as plt

def visualize():
    X = np.linspace(0,1,100)

    # Function derivative
    fx = np.cos(X**2)*2*X

    #Forward finite difference
    dfx = [(np.sin((x+0.01)**2) - np.sin(x**2))/0.01 for x in X]

    #visualization
    plt.plot(X,fx,c='g',marker= '+',label = 'True')
    plt.plot(X,dfx,c='b',label = '1st approx')
    plt.xlabel('x')
    plt.ylabel('dfx')
    plt.legend()
    plt.title('Actual and forward finite difference approximation')
    plt.show()

if __name__ =="__main__":
    #pass
    visualize()
