import math
import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt



def Newton_Raphson_method(X):
    F = []
    f = np.inf
    F.append(f)
    i = 0
    p= 0.1
    while f > 10**-6:
        X = X - np.matmul(Jacobinv(X),Function(X))
        f = scipy.linalg.norm(Function(X),2)
        F.append(f)
        if abs(F[-1] -F[-2]) < 10**-6:
            break
        i+=1
    #print(Function(X))
    #print(X)
    return F[1:]

def Function(X):
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    
    f1 = 3*x1 - math.cos(x2*x3) - 1.5
    f2 = 4*x1**2 - 625*x2**2 + 2*x3 - 1
    f3 = 20*x3 + math.exp(-x1*x2) + 9
    
    return np.array([f1,f2,f3])


def Jacobinv(X):
    
    x1 = X[0]
    x2 = X[1]
    x3 = X[2]
    
    df1x1 = 3
    df1x2 = x3*math.sin(x2*x3)
    df1x3 = x2*math.sin(x3*x2)
    
    df2x1 = 8*x1
    df2x2 = -1250*x2
    df2x3 = 2
    
    df3x1 = -x2*math.exp(-x1*x2)
    df3x2 = -x1*math.exp(-x2*x1)
    df3x3 = 20
    
    J = np.array([[df1x1,df1x2,df1x3],[df2x1,df2x2,df2x3],[df3x1,df3x2,df3x3]])
    
    return np.linalg.pinv(J)

if __name__=="__main__":
    
    #F = Newton_Raphson_method(np.array([1,1,1]))
    #plt.plot(F)
    #plt.xlabel("No of iterations")
    #plt.ylabel("F(X)")
    #plt.show()
    pass




    
