import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def func(t,y,mu):
    dydt = [y[1], mu[0]*(1 - y[0]**2)*y[1] - y[0]]
    return dydt

def Vander_pol_oscillator(mu):
    tspan = np.linspace(0, 20, 50)

    x0 = 1
    v0 = math.sqrt(4 - x0**2)
    yinit = [x0, v0]

    c = [mu]

    sol = solve_ivp(lambda t, y: func(t, y, c), [tspan[0], tspan[-1]], yinit, t_eval=tspan)

    T = sol.t
    X = sol.y[0]
    plt.plot(T,X)
    plt.xlabel('time')
    plt.ylabel('position')
    plt.title('Van der Pol Oscillator for mu = {}'.format(mu))
    plt.show()
    
    I = []
    for i in range(1, len(X)):
        if X[i]*X[i-1] < 0:
            I.append((T[i]+T[i-1])/2)
    j = 0
    Timeperiod = 0
    for i in range(2,len(I)):
        if Timeperiod == I[i] - I[i-2]:
            print(Timeperiod)
        else:
            Timeperiod = I[i] - I[i-2]
    return Timeperiod

if __name__=="__main__":
    #print("Time Period = ",Vander_pol_oscillator(1))
    pass
    

