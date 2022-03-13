from collections import defaultdict
import matplotlib.pyplot as plt
import random
import numpy as np
import math

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
    
    def bfs(self,node):
        graph = self.graph
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
        return visited
    
    def oneTwoComponentSizes(self):
        nodes = list(self.graph.keys())
        visited = self.bfs(nodes[0])
        sizes = []
        sizes.append(len(visited))
        for node in nodes:
            if node not in visited:
                v = self.bfs(node)
                visited.extend(v)
                sizes.append(len(v))
        sizes.sort(reverse=True)
        return sizes[:2]


class RandomGraph(UndirectedGraph):
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

    
if __name__ == "__main__":
    
    #g = UndirectedGraph(6)
    #g = g + (1, 2)
    #g = g + (3, 4)
    #g = g + (6, 4)
    #print(g.oneTwoComponentSizes())
    
    #g = RandomGraph(100)
    #g.sample(0.01)
    #print(g.oneTwoComponentSizes())
    

    #Largest = []
    #_2ndLargest = []
    #P = np.linspace(0,.01,50)
    #for p in P:
        #l1 = 0
        #l2 = 0
        #for i in range(50):
            #g = RandomGraph(1000)
            #g.sample(p)
            #l = g.oneTwoComponentSizes()
            #l1 += l[0]
            #try:
                #l2 += l[1]
            #except:
                #l2 +=0
        #Largest.append(l1/50)
        #_2ndLargest.append(l2/50)
    #plt.plot(P,Largest,c = 'g',label = 'Largest connected components')
    #plt.plot(P,_2ndLargest, c = 'b',label = '2nd largest connected component')
    #plt.axvline(x = math.log(1000)/1000 ,c = 'r',label='connectedness threshold')
    #plt.axvline(x = 0.001 ,label='Largest threshold')

    #plt.legend()
    #plt.xlabel('p')
    #plt.ylabel('fraction of runs G(100,p) is connected')
    #plt.title('Connectedness of a G(100,p) as a function of p')
    #plt.show()
        
