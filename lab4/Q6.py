import numpy as np
import matplotlib.pyplot as plt


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
            cof = [a + b for a, b in zip(self.cof, val.cof)]
            return self.__class__(cof)
        else:
            raise ValueError("addition with type {} not supported".format(type(val)))
        
    def __sub__(self,val):
        if isinstance(val, Polynomal):
            cof = [a - b for a, b in zip(self.cof, val.cof)]
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
        plt.show()
    
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
    
    
if __name__ =="__main__":
    
    #p = Polynomal([1, 2, 3])
    #pd = p.derivative()
    #print(pd)
    
    #p = Polynomal([1, 2, 3])
    #print(p.area(1,2))
    pass
    
