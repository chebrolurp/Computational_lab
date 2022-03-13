import matplotlib.pyplot as plt
import random

class Dice:
    def __init__(self,numSides=6):
        self.n = numSides
        self.vaild = self.validate(self.n)
        self.Probs = self.defaultProbs()
    def __str__(self):
        return "Dice with {} faces and probability distribution {}".format(self.n,self.Probs)
    
    # Checking the possibility of given number of sides
    def validate(self,n):
        if n < 4 or type(n) != int:
            raise Exception('Cannot construct the dice')
        else:
            return True
        
    # Default probabilities
    def defaultProbs(self):
        n = self.n
        p = [round(1/n,2) for i in range(self.n)]

        return p
    
    def setProb(self,probs):
        if len(probs) != self.n or sum(probs) != 1 :
            raise Exception('Invalid probability distribution') 
        else:
            self.Probs = list(probs)
            
    def roll(self,trails):
        
        cdf = [sum(self.Probs[:i]) for i in range(self.n+1)]
        
        outcome =[]
        expected = []
        
        for i in range(trails):
            x = random.uniform(0,1)
            for i in range(self.n):
                if x < cdf[i+1] and x > cdf[i]:
                    outcome.append(i+1)
                    break
        for i in range(1,self.n+1):
            for j in range([round(trails*p) for p in self.Probs][i-1]):
                expected.append(i)
        
        plt.hist(outcome,align='left',label='Actual')
        plt.hist(expected,align='right',label='Expected')
        plt.legend()
        plt.title('Outcome of {} throws of a {}-faced dice'.format(trails,self.n))
        plt.xlabel('Sides')
        plt.ylabel('Occurances')
        plt.show()
        
if __name__=='__main__':
    d = Dice(4)
    d.setProb((0.1,0.2,0.3,0.4))
    d.roll(1000)
