import random
import math
import numpy as np


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
        
    def derivative(self):
        cof = [i*cof for i,cof in enumerate(self.cof)]
        return self.__class__(cof[1:])
        
    def area(self,a,b):
        area = 0
        for i,cof in enumerate(self.cof):
            j = i+1
            area+= cof*(b**j - a**j)/j
        return 'Area in the intervel [{},{}] is: {}'.format(a,b,area)
    
    def printroots(self):
        
        degree = len(self.cof)-1
        coef = self.cof
        upper = 1 + 1 / abs(coef[-1]) * max(abs(coef[x]) for x in range(degree))
        lower = abs(coef[0]) / (abs(coef[0]) + max(abs(coef[x]) for x in range(1, degree + 1)))
        
        # Initalize roots
        roots = []
        for i in range(degree):
            radius = random.uniform(lower, upper)
            angle = random.uniform(0, 2*math.pi)
            root = complex(radius * math.cos(angle), radius * math.sin(angle))
            roots.append(root)
        
        
        dP = self.derivative()
        while True:
            valid = 0
            for k, r in enumerate(roots):
                ratio =  self[r] / dP[r]
                offset = ratio / (1 - (ratio * sum(1/(r - x) for j, x in enumerate(roots) if j != k)))
                if round(offset.real, 4) == 0 and round(offset.imag, 4) == 0:
                    valid += 1
                roots[k] -= offset
            if valid == len(roots):
                break

        print("The roots of the polynomial are: \n",[complex(round(r.real, 4), round(r.imag, 4)) for r in roots])
        
        
        
if __name__=="__main__":
    P = Polynomal([1,2,3,4,5,6,7])
    P.printroots()
