import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import math



def Heat_equation(xc,yc):
    T = np.linspace(0,.1,200)
    X1 = np.linspace(0,1,40)
    X2 = np.linspace(0,1,40)

    # Intial conditions
    U = np.zeros(shape = (len(X1),len(X2),len(T)))

    # Boundary conditions
    U[:, -1, :] = 0
    U[:, 0, :] = 0
    U[-1, :, :] = 0
    U[0, :, :] = 0

    

    lambd = 0.25


    for k in range(0, len(T)-1):
        for i in range(1, len(X1)-1):
            for j in range(1, len(X2)-1):
                U[i, j,k+1] = lambd * (U[i+1][j][k] + U[i-1][j][k] + U[i][j+1][k] + U[i][j-1][k] - 4*U[i][j][k]) + U[i][j][k] + dt*math.exp(-math.sqrt((i-xc)**2 + (j-yc)**2))

        

    def animation_frame(k):
        plt.clf()
        plt.imshow(U[:,:,k],cmap="hot")
        plt.title('the Temperature distribution after {} time'.format(k))
        return plt,

    anim = FuncAnimation(plt.figure(), func=animation_frame, frames=np.arange(0, len(T)),interval = 1)
    plt.show()
    
Heat_equation(10,10)



