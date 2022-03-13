from collections import defaultdict
import matplotlib.pyplot as plt

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

if __name__ == '__main__':
    pass
    
    #g = UndirectedGraph(5)
    #g = g + (1, 2)
    #g = g + (3, 4)
    #g = g + (1, 4)
    #print(g)
    
    #g = UndirectedGraph()
    #g = g + 100
    #g = g + (1,2)
    #g = g + (1,100)
    #g = g + (100,3)
    #g = g + 20
    #g.plotDegDist()
