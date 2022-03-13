import networkx as nx
import random
import matplotlib.pyplot as plt
import math
import numpy as np

class Lattice:
    def __init__(self,N):
        self.dim = N
        
        Graph = nx.grid_2d_graph(N,N)
        
        
        Graph.clear_edges()
        self.G = Graph
        
        for edge in list(self.G.edges):
            Graph.remove_edge(edge[0],edge[1])
        self.Gc = Graph
        
        self.B = [(i,0) for i in range(self.dim)]
        
        self.T = [(i,self.dim-1) for i in range(self.dim)]
        
    def show(self):
        plt.figure(figsize=(8,8))
        N = self.dim
        G = self.G
        pos = dict( (n, n) for n in G.nodes() )
        nx.draw_networkx_nodes(G, pos, node_size=0.1, node_color='r')
        nx.draw_networkx_edges(G,pos,edge_color='r')
        #nx.draw(G, pos=pos,node_size=10)
        plt.axis('off')
        plt.show()
    
    def percolate(self,p):
        nodes = list(self.G.nodes())
        for node in nodes:
            x,y = node
            if x == self.dim - 1 and y == self.dim-1:
                continue
            elif x== self.dim -1:
                nei = [(x,y+1)]
            elif y == self.dim -1:
                nei = [(x+1,y)]
            else:
                nei = [(x+1,y),(x,y+1)]
            for n in nei:
                x = random.random()
                if x < p:
                    self.G.add_edge(node,n)
                        
                        
    def existsTopDownPath(self):
        # complement graph
        bottom_nodes = self.B 
        top_nodes = self.T
        for Tnode in top_nodes:
            for Bnode in bottom_nodes:
                if nx.has_path(self.Gc,Tnode,Bnode):
                    return True
        return False
                
    def showPaths(self):
        Gc = self.Gc
        bottom_nodes = self.B 
        top_nodes = self.T
        G = self.G
        pos = dict( (n, n) for n in G.nodes() )
        nx.draw_networkx_nodes(G, pos, node_size=0.1, node_color='r')
        nx.draw_networkx_edges(G,pos,edge_color='r')
        
        for Tnode in top_nodes:
            minpath = None
            minlength = math.inf
            for Bnode in bottom_nodes:
                try:
                    path = nx.shortest_path(l.Gc,source=Tnode,target=Bnode)
                    length = nx.shortest_path_length(l.Gc,source=Tnode,target=Bnode)
                    if length < minlength:
                        minpath = path
                        minlength = length
                except:
                    continue
            if minpath == None:
                d = nx.single_source_shortest_path_length(l.Gc, Tnode)
                node = max(d, key=d.get)
                path = nx.shortest_path(Gc,source=Tnode,target=node)
                path_edges = list(zip(path,path[1:]))
            else:
                path = minpath
                path_edges = list(zip(path,path[1:]))
            nx.draw_networkx_edges(Gc,pos,edgelist=path_edges,edge_color='g')
        plt.show()
        
        
if __name__ =="__main__":
    

    
    #P1 = np.linspace(0,0.4,10)
    #P2 = np.linspace(0.4,0.6,10)
    #P3 = np.linspace(0.6,1,10)
    #P = np.concatenate((P1,P2,P3))
    #perOccured = []
    #for p in P:
        #O = 0
        #for i in range(50):
            #l = Lattice(100)
            #l.percolate(p)
            #if l.existsTopDownPath():
                #O+=1
        #perOccured.append(O/50)
    #plt.plot(P,perOccured)
    #plt.xlabel('p')
    #plt.ylabel('Fraction of runs end-to-end percolation occurred')
    #plt.title('Critical cut-off in 2-D bond percolation')
    #plt.show()
    
    
    
