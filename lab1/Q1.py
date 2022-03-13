import math
import matplotlib.pyplot as plt


# Error in  Stirling's approximation
def StirlingFormulae(n):
    error = math.log(math.factorial(n))+n - math.log(math.sqrt(2*math.pi*n)) - n*math.log(n)
    return error

N = [10**i for i in range(7)]

Error = [StirlingFormulae(n) for n in N]

# Plotting in log scale
plt.plot(N,Error)
plt.title('Error in approximation ')
plt.xscale('log')
plt.xlabel('n')
plt.ylabel('error')
plt.show()
