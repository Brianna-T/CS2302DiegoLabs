"""
Tovar, Brianna
CS2302 Aguirre Diego, TA Eduardo
11/30
Lab 6: Kruskal's Algorithm and Topological Sort
"""

from collections import defaultdict 


class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        """
        dictionary used to contain the list of edges, vertices as an AL
        """
        self.vertices = vertices 
  
    def addEdge(self,u,v):
        """
        Appending, adding, vertices in graph
        Ex: u=5, position 5 will have v=0, vertex 0
        Creates the edge
        """
        self.graph[u].append(v)
        
    def topologicalSort(self): 
        """
        vertices set to not visited since we are starting
        """
        visited = [False]*self.vertices 
        stack =[]
        """
        using stack, problems with using code given by
        professor (using queues) so I'm using a new approach
        """
        for i in range(self.vertices):
            """
            traversing thru number of vertices, checking
            if false, and if is, goes to helper method
            """
            if visited[i] == False: 
                    self.topologicalSortUtil(i,visited,stack) 
  

        print(stack)
        

    def topologicalSortUtil(self,v,visited,stack):
        """
        this is our visited list: visited=[False]*self.vertices
        with [v]=i from self.topo..(i,visited,stack)
        this'll set our not visited list at index v from previous for-loop to be True
        """
        visited[v] = True
  
        """
        traversing using v=i from previous for loop
        """
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) #recursion to change to True
  
        #inserting vertex into stack
        stack.insert(0,v) 

        
g= Graph(6) 
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
  
print("Resulted Graph")
g.topologicalSort() 


class Graph: 
    """
    another graph needed for Kruskal's Algorithm
    """
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] #default dict
          
   
    def addEdge(self,u,v,w): 
        """
        appends the two vertices and the weight given
        """
        self.graph.append([u,v,w])
 
    def Kruskal(self): 
  
        result =[] #resulted list
  
        """
        Sort all the edges in order 
        order of their weight, and create a copy of graph
        so not to alter it
        """
        self.graph =  sorted(self.graph)
        #unifinished
  

g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

print("New graph, weighted")
print(g.graph)

g.Kruskal() 