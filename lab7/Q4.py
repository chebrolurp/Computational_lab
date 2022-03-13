import math
import numpy as np
import matplotlib.pyplot as plt


def Secant_method(x0,x1):
    F = []
    while function(x1) > 10**-6:
        x = x1 - function(x1)*(x1 - x0)/(function(x1) - function(x0))
        x0 = x1
        x1 = x
        F.append(function(x1))
    return F

def Newton_Raphson_method(x0):
    F = []
    while function(x0) > 10**-6:
        x0 = x0 - function(x0)/function_derivative(x0)
        F.append(function(x0))
    
    return F

def function(x):
    
    f = math.cos(x)+2*math.sin(x)+x**2
    
    return f

def function_derivative(x):
    
    df = - math.sin(x) + 2*math.cos(x) + 2*x
    
    return df
    
    
if __name__=="__main__":
    Fs = Secant_method(3,3.1)
    Fn = Newton_Raphson_method(3)

    plt.plot(Fn[2:], label ="Newton-Raphson method")
    plt.plot(Fs[2:], label = "Secant method")
    plt.title("convergence rate")
    plt.legend()
    plt.show()
