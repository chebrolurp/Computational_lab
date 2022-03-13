import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import interpolate
x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(-4, 4)
line, = ax.plot(0, 0,label = "True")
line1, = ax.plot(0, 0,label = 'Cubic Spline')
line2, = ax.plot(0, 0,label = 'Barycentric')
line3, = ax.plot(0, 0,label = 'Akime')

def animation_frame(i):
    x = np.linspace(0,1,100)
    y = np.tan(x)*np.sin(30*x)*np.exp(x)
    tck = interpolate.splrep(x, y, s=0)
    xnew = np.linspace(0,1,i)
    ynew = interpolate.splev(xnew, tck)
    y_bary= interpolate.barycentric_interpolate(xnew,np.tan(xnew)*np.sin(30*xnew)*np.exp(xnew) ,x)
    Akime = interpolate.Akima1DInterpolator(xnew,np.tan(xnew)*np.sin(30*xnew)*np.exp(xnew))
    y_akime = Akime(x)
    
    line.set_xdata(x)
    line.set_ydata(y)
    
    line1.set_xdata(xnew)
    line1.set_ydata(ynew)
    
    line2.set_xdata(x)
    line2.set_ydata(y_bary)
    
    line3.set_xdata(x)
    line3.set_ydata(y_akime)
    plt.title("Different interpolations of tan(x).sin(x).exp(x) for {} samples".format(i))
    
    return line, line1, line2, line3,

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(2, 40, 1),interval = 500)
plt.legend()
plt.xlabel('x')
plt.ylabel('fx')
plt.show()
