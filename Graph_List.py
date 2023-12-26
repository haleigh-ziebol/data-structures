class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
        
    def add_edge(self, node1, node2):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
        
    def display_graph(self):
        for node in self.adjacency_list:
            print(node, '->', ' -> '.join(map(str, self.adjacency_list[node])))


my_graph = Graph()
my_graph.add_node('A')
my_graph.add_node('B')
my_graph.add_node('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')

my_graph.display_graph()