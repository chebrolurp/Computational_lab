import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

Theta = []
T = []
v0 = 0
theta0 = math.pi/8
V = [] 
t = 0
h = .05
g = 9.8
L = 2
TimePeriod = 2*math.pi*math.sqrt(L/g)
while t < 3*TimePeriod:
    Theta.append(theta0)
    V.append(v0)
    T.append(t)
    t += h 
    theta0 = theta0 - h*v0
    v0 = v0 + h*g*math.sin(theta0)/L

x_data = [0,0]
y_data = [0,0]

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5,1)
line0, = ax.plot([-0.5,0.5],[0,0],'black',linewidth = 2)
line, = ax.plot(0, 0,linewidth = 3)
#line1, = ax.plot(0, 0,marker = 'o',markersize = 5)
line2, = ax.plot(0, 0,marker = 'o',markersize = 10,color = 'r')

def animation_frame(i):
    x = L*np.sin(Theta[i])
    y = -L*np.cos(Theta[i])

    x_data[1] = x
    y_data[1] = y

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    
    line2.set_xdata(x)
    line2.set_ydata(y)
    return line, 

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, len(Theta)),interval = 10)
plt.show()
