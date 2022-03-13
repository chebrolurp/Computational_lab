from collections import defaultdict
import matplotlib.pyplot as plt
import math
import numpy as np


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
        
    def isConnected(self, vertices_encountered = None, start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.graph       
        vertices = list(gdict.keys()) # "list" necessary in Python 3 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.isConnected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False
    
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
                    
    def isConnected(self):
        graph = self.graph
        nodes = list(graph.keys())
        node = nodes[0]
        queue = []
        visited = []
        # starting node
        queue.append(node)
        visited.append(node)
        while queue:
            s = queue.pop(0) 
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        if len(visited)== len(nodes):
            return True
        else:
            return False
    
if __name__ =="__main__":
    pass
    
    #g = UndirectedGraph(5)
    #g = g + (1, 2)
    #g = g + (2, 3)
    #g = g + (3, 4)
    #g = g + (3, 5)
    #print(g.isConnected())
    
    

    #fracConnected = []
    #P = np.linspace(0,.1,50)
    #for p in P:
        #connected = 0
        #for i in range(1000):
            #g = ERRandomGraph(100)
            #g.sample(p)
            #if g.isConnected():
                #connected+=1
        #fracConnected.append(connected/100)
    #plt.plot(P,fracConnected)
    #plt.axvline(x = math.log(100)/100 ,c = 'r',label='Theoretical threshold')
    #plt.legend()
    #plt.xlabel('p')
    #plt.ylabel('fraction of runs G(100,p) is connected')
    #plt.title('Connectedness of a G(100,p) as a function of p')
    #plt.show()
    
