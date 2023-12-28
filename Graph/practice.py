class G:
    def __init__(self):
        self.graph = {}

    def print_graph(self):
        print('Graph contents : ', list(self.graph.keys()))

    def add_node(self, node):
        self.graph[node] = []
    
    def add_edge(self, n1 , n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)
        
    def DFS(self, start_node , visited = None):
        if visited is None:
            visited = set()
        
        print(start_node, end=' ')
        visited.add(start_node)
        for n in self.graph[start_node]:
            if n not in visited:
                self.DFS(n, visited)
        
    def BFS(self, start_node):
        visited , queue = set() , [start_node]
        
        while queue:
            cn = queue.pop(0)
            if cn not in visited:
                print(cn, end=' ')
                visited.add(cn)
                queue.extend(self.graph[cn])
                
    
            
    def cyclic_util(self, cn, visited, p=None):
        visited.add(cn)
        
        return any(
            n  not in visited
            and self.cyclic_util(n , visited , cn)
            or n in visited
            and n!=p
            for n in self.graph[cn]
        )
        
    def cycle(self):
        visited = set()
        return any(self.cyclic_util(n, visited) for n in self.graph)
    
    
    
        


g = G()


for i in range(1,6):
    g.add_node(i)
g.add_edge(1,2)
g.add_edge(2,1)
g.add_edge(3 , 1)
g.add_edge(1 , 5)

g.print_graph()
g.DFS(1)
print()
g.BFS(1)
print()
print('Is the graph cyclic? - >', g.cycle())
