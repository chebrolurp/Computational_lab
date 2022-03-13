import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fftpack import fft, ifft
import random


class Polynomal(object):
    def __init__(self,cof):
        self.cof = cof
    def __str__(self):
        string = "Coefficients of the polynomial are:\n"
        for i in self.cof:
            string += '{} '.format(i)
        string.strip()
        return string
    def __add__(self,val):
        if isinstance(val, Polynomal):
            l1 = len(val.cof)
            l2 = len(self.cof)
            if l1 >= l2:
                cof = val.cof
                for i in range(l2):
                    cof[i] = cof[i] + self.cof[i]
            else:
                cof = self.cof
                for i in range(l1):
                    cof[i] = cof[i] + val.cof[i]
            return self.__class__(cof)
        else:
            raise ValueError("addition with type {} not supported".format(type(val)))
        
    def __sub__(self,val):
        if isinstance(val, Polynomal):
            l1 = len(val.cof)
            l2 = len(self.cof)
            if l1 >= l2:
                cof = val.cof
                for i in range(l2):
                    cof[i] = cof[i] - self.cof[i]
            else:
                cof = self.cof
                for i in range(l1):
                    cof[i] = cof[i] - val.cof[i]
            return self.__class__(cof)
        else:
            raise ValueError("Subtraction with type {} not supported".format(type(val)))
    
    def __mul__(self,val):
        if isinstance(val, (int, float)):
            cof = [a *  val for a in self.cof]
            return self.__class__(cof)
        elif isinstance(val, Polynomal):
            cof = [0]*(len(val.cof)+len(self.cof)-1)
            for i in range(len(val.cof)):
                for j in range(len(self.cof)):
                    cof[i+j] += val.cof[i] * self.cof[j]
            return self.__class__(cof)
        else:
            raise ValueError("multiplication with type {} not supported".format(type(val)))
        
    def __rmul__(self, val):
        return self.__mul__(val)
        
    def __getitem__(self,x):
        return sum((x**i)*c for i,c in enumerate(self.cof))
        
    def show(self,a,b):
        X = list(np.linspace(a,b,50))
        fx = []
        for x in X:
            fx.append(self[x])
        plt.plot(X,fx)
        plt.xlabel('x')
        plt.ylabel('F(x)')
        #plt.title('Polynomial Plot')
        #plt.show()
    
    def fitViaMatrixMethod(self,points):
        n = len(points)
        A = []
        b = []
        X = []
        for i in range(n):
            x,y = points[i]
            X.append(x)
            b.append(y)
            A.append([x**i for i in range(n)])
        self.cof = np.linalg.solve(np.array(A),np.array(b))
        plt.scatter(X,b,c='r')
        plt.title('Polynomial interpolation using matrix method')
        self.show(min(X),max(X))  
    
    def fitViaLagrangePoly(self,points):
        n = len(points)
        P = self.__class__([0 for i in range(n)])
        fx = []
        X = []
        for i in range(n):
            x,y = points[i]
            X.append(x)
            fx.append(y)
        for i in range(n):
            p = self.__class__([1])
            for j in range(n):
                if i!=j:
                    p = p * self.__class__([-X[j]/(X[i]-X[j]),1/(X[i]-X[j])]) 
            P = P + fx[i]*p
            
        self.cof = P.cof
        plt.scatter(X,fx,c='r')
        plt.title('Polynomial interpolation using Lagrange method')
        self.show(min(X),max(X))
        
    def derivative(self):
        cof = [i*cof for i,cof in enumerate(self.cof)]
        return self.__class__(cof[1:])
        
    def area(self,a,b):
        area = 0
        for i,cof in enumerate(self.cof):
            j = i+1
            area+= cof*(b**j - a**j)/j
        return 'Area in the intervel [{},{}] is: {}'.format(a,b,area)
    
    
    
    
    



def Multiply(A,B):
    n1 = A
    n2 = B
    lA =[]
    while(A):
        lA.append(A%10.0)
        A = A//10
        
    lB =[]
    while(B):
        lB.append(B%10.0)
        B = B//10
        
    l = max(len(lA),len(lB))
    lA = lA +[0.0 for i in range(2*l - len(lA))]
    pA = Polynomal(lA)


    lB = lB + [0.0 for i in range(2*l - len(lB))]
    pB = Polynomal(lB)
    fftA = fft(lA)
    fftB = fft(lB)
    fftP = ifft(fftA*fftB)
    fftp = [np.round(t,0) for t in fftP]
    
    P = n1*n2
    print("1st number:", n1)
    print("2nd number:",n2)
    print("Product using fft:",Polynomal(fftp)[10].real)
    print("error in multiplication is = ", 100*(Polynomal(fftp)[10].real-P)/P)
    
    
if __name__=="__main__":
        
    # 2 large n digir integers
    #A = random.randint(1e130,1e141)
    #B = random.randint(1e130,1e141)
    #Multiply(A,B)
    pass
    
    
