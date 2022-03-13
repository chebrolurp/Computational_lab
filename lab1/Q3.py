import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo Simulation
def estimatePi(n):
    count = 0
    for i in range(n):
        # x and y in range [-1,1]
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        
        # Points inside the circle with center origin
        if (x**2+y**2) < 1:
            count+=1
    return 4*count/n

print('It might take a while, please wait .....')
N = np.linspace(0,2*10**6,1000,dtype='int')
pi = [estimatePi(n) for n in N]

# Plot
plt.axhline(y=math.pi, color='r', linestyle='-',label='value of math.pi')
plt.plot(N,pi,label='Monte Carlo method')
plt.title('Estimating pi using Monte Carlo Method')
plt.xlabel('No. of points')
plt.ylabel('value of pi')
plt.legend()
plt.show()
