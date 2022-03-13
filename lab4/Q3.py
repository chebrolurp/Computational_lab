import numpy as np
import matplotlib.pyplot as plt

def visualize():
    H = np.linspace(0.0001,1,100)
    mefx1 = []
    met1=[] 
    mefx2 = []
    met2 = []
    X = np.linspace(0,1,100)

    # function derivate
    fx = np.cos(X**2)*2*X

    for h in H:
        # max of Absolute error for forward finite difference
        efx1 = np.abs(fx - np.array([(np.sin((x+h)**2) - np.sin(x**2))/h for x in X]))
        mefx1.append(max(efx1))
        #theoretical max of Absolute error
        met1.append(max(np.abs(h*(np.cos(X**2) - 2*X**2*np.sin(X**2)))))
        # Absolute error for center finite difference
        efx2 = np.abs(fx - np.array([(np.sin((x+h)**2) - np.sin((x-h)**2))/(2*h) for x in X]))
        
        # max of Absolute error for center finite difference
        mefx2.append(max(efx2))
        #theoretical max of Absolute error
        met2.append(max(np.abs(h**2*(4*X*np.sin(X**2) + 8*X**3*np.cos(X**2) +  8*X*np.sin(X**2))/6)))



    plt.plot(H,mefx1,c='b',label = 'forward numerical')
    plt.plot(H,met1,c='g',label = 'forward theoretical')
    plt.plot(H,mefx2,c='r',label = 'central numerical')
    plt.plot(H,met2,c='y',label = 'central theoretical')
    plt.xlabel('h')
    plt.ylabel('error')
    plt.title('Maximum absolute error of approximations')
    plt.legend()
    plt.show() 

if __name__ == "__main__":
    pass
    #visualize()
