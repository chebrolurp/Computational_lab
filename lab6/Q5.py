import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#import matplotlib.animation as animation
import numpy as np
import scipy
from scipy.integrate import odeint



def ThreeBodyEquations(w,t):
    r1=w[:2]
    r2=w[2:4]
    r3=w[4:6]
    v1=w[6:8]
    v2=w[8:10]
    v3=w[10:12]    
    r12=scipy.linalg.norm(r2-r1)
    r13=scipy.linalg.norm(r3-r1)
    r23=scipy.linalg.norm(r3-r2)
    
    dv1bydt = (r2-r1)/r12**3 + (r3-r1)/r13**3
    dv2bydt = (r1-r2)/r12**3+ (r3-r2)/r23**3
    dv3bydt = (r1-r3)/r13**3+ (r2-r3)/r23**3
    dr1bydt = v1
    dr2bydt = v2
    dr3bydt = v3
    
    derivs = np.concatenate((dr1bydt,dr2bydt,dr3bydt,dv1bydt,dv2bydt,dv3bydt))
    
    return derivs




r1 = [0, 1]
r2 = [1, 0] 
r3 = [1, 1]
r1 = np.array(r1,dtype="float64")
r2 = np.array(r2,dtype="float64")
r3 = np.array(r3,dtype="float64")
v1 = [0.01, -0.01] 
v2 = [0, 0] 
v3 = [0 , 0.01]
v1 = np.array(v1,dtype="float64")
v2 = np.array(v2,dtype="float64")
v3 = np.array(v3,dtype="float64")


#Package initial parameters
init_params = np.array([r1,r2,r3,v1,v2,v3])
#Flatten to make 1D array
init_params = init_params.flatten() 
time_span = np.linspace(0,10,500) 
three_body_sol = odeint(ThreeBodyEquations,init_params,time_span)

x1 = three_body_sol[:,0]
y1 = three_body_sol[:,1]
x2 = three_body_sol[:,2]
y2 = three_body_sol[:,3]
x3 = three_body_sol[:,4]
y3 = three_body_sol[:,5]


x_data = [0,0]
y_data = [0,0]

fig, ax = plt.subplots()
ax.set_xlim(min(np.concatenate([x1,x2,x3]))-1, max(np.concatenate([x1,x2,x3]))+1)
ax.set_ylim(min(np.concatenate([y1,y2,y3]))-1, max(np.concatenate([y1,y2,y3]))+1)
line0, = ax.plot(x1[0], y1[1],marker = 'o',markersize = 5,color = 'r')
line1, = ax.plot(x2[0], y2[1],marker = 'o',markersize = 5,color = 'g')
line2, = ax.plot(x3[0], y3[1],marker = 'o',markersize = 5,color = 'b')

def animation_frame(i):

    line0.set_xdata(x1[i])
    line0.set_ydata(y1[i])
    
    line1.set_xdata(x2[i])
    line1.set_ydata(y2[i])
    
    line2.set_xdata(x3[i])
    line2.set_ydata(y3[i])
    
    return line0,line1,line2

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, len(x1)),interval = 10)


#FFwriter = animation.FFMpegWriter()
#anime.save('animation.mp4', writer = FFwriter)
plt.show()









