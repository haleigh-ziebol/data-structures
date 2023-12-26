class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination):
        self.graph[source][destination] = 1 #updates matrix
        self.graph[destination][source] = 1 # updates matrix
    
    def display(self): # print rows in matrix
        for row in self.graph:
            print(" ".join(map(str, row)))
    

graph = Graph(4) #4 nodes
#add edges
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,2)
graph.add_edge(2,3)

graph.display()