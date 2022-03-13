import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T = np.linspace(0,.5,2000)
X = np.linspace(0,1,10)
U = np.zeros(shape = (len(X),len(T)))

U[:,0] = np.exp(-X)


k = T[1] - T[0]
h = X[1] - X[0]


# Boundary conditions
U[0,:] =  2*U[1,:] - U[2,:]
U[-1,:] = 2*U[-2,:] - U[-3,:]

lambd =k/h**2

for k in range(0, len(T)-1):
    for i in range(1, len(X)-1):
        U[i, k+1] = lambd*U[i-1, k] + (1-2*lambd)*U[i,k] + lambd*U[i+1,k] 

fig, ax = plt.subplots()
ax.set_xlim(0,1)
ax.set_ylim(0,1)
x = np.linspace(0,1,10)
line0, = ax.plot(x,U[:,0],'black',linewidth = 2)


def animation_frame(i):
    
    line0.set_xdata(x)
    line0.set_ydata(U[:,i])
    if i%100==0:
        plt.title("Temperature distribution after t = {} unit".format(i/4000))
    return line0, 

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, len(T)),interval = 10)
plt.show()
