class graph(self):
    self.adj_list={}

def print_graph(self):
    for vertex in self.adj_list:
        print(vertex,":",self.adj_list[vertex])

def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
def add_edge(self,v1,v2):
    if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)
        return True
return False

my_graph = graph()
my_graph.add_vertex(v1)
my_graph.add_vertex(v2)
my_graph.add_edge(v1,v2)
