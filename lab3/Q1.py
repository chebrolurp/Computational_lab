
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
    
if __name__ =="__main__":
    
    #r = RowVectorFloat([1, 2, 4])
    #print(r)
    #print(len(r))
    #print(r[1])
    #r[2] = 5
    #print(r)
    
    #r1 = RowVectorFloat([1, 2 , 4])
    #r2 = RowVectorFloat([1, 1 , 1])
    #r3 = 2*r1 + (-3)*r2
    #print(r3)
    
