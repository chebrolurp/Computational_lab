import random
import numpy as np
import matplotlib.pyplot as plt

class RowVectorFloat(object):
    
    def __init__(self,l):
        self.v = l
        
    def __getitem__(self,index):
        return self.v[index]
    
    def __setitem__(self,index,value):
        self.v[index]=value
        return
    
    def __len__(self):
        return len(self.v)
    
    def __str__(self):
        string = ""
        for i in self.v:
            string += '{:.2f} '.format(i)
        string.strip()
        return string
    
    def __rmul__(self, val):
        return self.__mul__(val)
        
    def __mul__(self,val):
        if isinstance(val, RowVectorFloat):
            v = [a * b for a, b in zip(self, val)]
            return sum(v)
        elif isinstance(val, (int, float)):
            v = [val*e for e in self.v]
            return self.__class__(v)
        else:
            try:
                raise Exception
            except:
                print(Exception)
                raise ValueError("Multiplication with type {} not supported".format(type(val)))
   
    def __add__(self,val):
        if isinstance(val, RowVectorFloat):
            v = [a + b for a, b in zip(self, val)]
            return self.__class__(v)
        elif isinstance(val, (int, float)):
            v = [a + val for a in self]
            return self.__class__(v)
        else:
            try:
                raise Exception
            except:
                print(Exception)
                raise ValueError("addition with type {} not supported".format(type(val)))
            
    def __radd__(self, other):
        return self.__add__(other)
    
    
class SquareMatrixFloat:
    def __init__(self,n):
        self.n = n
        matrix = [RowVectorFloat([0 for i in range(n)]) for j in range(n)]
        self.m = matrix
    def __str__(self):
        print("The Matrix is")
        for r in self.m:
            print(r)
        return ""
    
    def sampleSymmetric(self):
        for i in range(self.n):
            for j in range(i,self.n):
                if i == j:
                    self.m[i][j] = random.uniform(1,self.n)
                else:
                    self.m[i][j] = self.m[j][i] = random.uniform(0,1)
        return
    
    def toRowEchelonForm(self):
        matrix = []
        for i,j in enumerate(self.m):
            j = (1/j[i])*j + 0
            matrix.append(j)
            for k in range(i+1,self.n):
                self.m[k] += (-self.m[k][i])*j
        self.m = matrix
        
    def isDRDominant(self):
        for i,r in enumerate(self.m):
            if 2 * r[i] >= sum(r.v):
                continue
            else:
                return False
        return True
                
    def jSolve(self,b,m):
        if self.isDRDominant():
            X_init = [random.random() for i in range(self.n)]
            error = []
            for i in range(m):
                X = []
                e = 0
                for j in range(self.n):
                    r = [s.m[j][k]*X_init[k] for k in range(self.n) if j!=k]
                    er = b[j] - sum(r)
                    X.append(er/s.m[j][j])
                    err = b[j] - sum([s.m[j][k]*X_init[k] for k in range(self.n)])
                    e+= err**2
                X_init = X
                error.append(e)
            return error,X
        else:
            try:
                raise Exception
            except:
                print(Exception)
                print('Not solving because convergence is guranteed.')
            return "",""
        
    def gsSolve(self,b,m):
        if self.isDRDominant():
            X_init = [random.random() for i in range(self.n)]
            error = []
            for i in range(m):
                X = []
                e = 0
                for j in range(self.n):
                    r1 = [s.m[j][k]*X[k] for k in range(j) if j!=k]
                    r2 = [s.m[j][k]*X_init[k] for k in range(j,self.n) if j!=k]
                    er = b[j] - sum(r1) - sum(r2)
                    X.append(er/s.m[j][j])
                    err = b[j] - sum([s.m[j][k]*X_init[k] for k in range(self.n)])
                    e+= err**2
                X_init = X
                error.append(e)
            return error,X
        else:
            try:
                raise Exception
            except:
                print(Exception)
                print('Not solving because convergence is guranteed.')
            return "",""
        
if __name__ =="__main__":
    
        
    #C = True
    #while(C):
        #s = SquareMatrixFloat(10)
        #s.sampleSymmetric()
        #if s.isDRDominant():
            #C = False
            #(err, x) = s.jSolve([i for i in range(1,11)], 10)
            #plt.plot([i for i in range(1,11)],err,label = 'Jacobi')
            #(err,x) =  s.gsSolve([i for i in range(1,11)], 10)
            #plt.plot([i for i in range(1,11)],err,label = 'Gauss-Siedel')
            #plt.title('Convergence Plot')
            #plt.xlabel('no of iterations')
            #plt.ylabel('error')
            #plt.legend()
            #plt.show()
            
    

