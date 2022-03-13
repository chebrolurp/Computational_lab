from collections import defaultdict
import matplotlib.pyplot as plt
import random

class UndirectedGraph:
    def __init__(self,N=None):
        self.graph = defaultdict(list)
        self.ristrict = False
        if N != None:
            self.ristrict = True
            for i in range(1,N+1):
                 self.graph[i]
    
    def addNode(self,node):
        if node > len(self.graph) and self.ristrict == True:
            try:
                raise 
            except Exception:
                print(Exception)
                print(Exception('Node index cannot exceed number of nodes'))
        self.graph[node]
        
    def addEdge(self,node1,node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
    
    def __add__(self, node):
        if type(node)==int:
            self.graph[node]
        else:
            node1,node2 = node
            self.addEdge(node1,node2)
        return self
    
    def __str__(self):
        string2 = ''
        Nedges = 0
        for i,j in self.graph.items():
            Nedges+=len(j)
            if len(j)==0:
                string2 = string2 + 'Node {}: '.format(i) + '{}' + '\n'
            else:
                string2 = string2 + 'Node {}: '.format(i) + str(set(j)) + '\n'
        string1 = 'Graph with {} nodes and {} edges. Neighbours of the nodes are belows:\n'.format(len(self.graph),int(Nedges/2))
        
        string = string1 + string2
            
        return string
   
    def plotDegDist(self):
        Nodes = len(self.graph)
        degree = []
        node_degree = [ i for i in range(Nodes)]
        for i,j in self.graph.items():
            degree.append(len(j))
        fracNodes=[]
        for i in range(Nodes):
            fracNodes.append(degree.count(i)/Nodes)
        Avg_node_degree = sum(degree)/Nodes
        plt.axvline(x = Avg_node_degree ,c = 'r',label='Avg. node degree')
        plt.scatter(node_degree,fracNodes,label='Actual degree distribution')
        plt.legend()
        plt.title('Node Degree Distribution')
        plt.show()
        
class ERRandomGraph(UndirectedGraph):
    def __init__(self,N):
        self.graph = defaultdict(list)
        self.p = None
        for i in range(1,N+1):
            self.graph[i]
    def sample(self,p):
        N = len(self.graph)
        for i in range(1,N):
            for j in range(i+1,N+1):
                x = random.random()
                if x < p:
                    self.graph[i].append(j)
                    self.graph[j].append(i)
                    
if __name__ =='__main__':
    pass
    # The following code creates a G(100, 0.7) random graph and
    # plots its degree distribution
    #g = ERRandomGraph(100)
    #g.sample(0.7)
    #g.plotDegDist()
    
    # The following code creates a G(1000, 0.4) random graph and
    # plots its degree distribution
    #g = ERRandomGraph(1000)
    #g.sample(0.4)
    #g.plotDegDist()
    
    
