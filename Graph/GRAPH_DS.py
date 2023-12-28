from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, n1, n2):
        if n1 not in self.graph or n2 not in self.graph:
            print('not in graph')
        else:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)

    def print_node(self):
        print('Nodes in the graph', list(self.graphs.keys()))

    def delete_node(self, node):
        del self.graph[node]
        for i in self.graph:
            self.graph[i] = [i for i in self.graph[i] if i != node]

    def delete_edge(self, n1, n2):
        self.graph[n1] = [i for i in self.graph[n1] if i != n2]
        self.graph[n2] = [i for i in self.graph[n2] if i != n1]

    def DFS(self, start_node, visited=None):
        if visited is None:
            visited = set()

        print(start_node, end=' ')
        visited.add(start_node)

        for neighbor in self.graph[start_node]:
            if neighbor not in visited:
                self.DFS(neighbor, visited)

    def BFS(self, start_node):
        visited,  queue = set(), [start_node]
        while queue:
            c_n = queue.pop(0)
            if c_n not in visited:
                print(c_n, end=' ')
                visited.add(c_n)
                queue.extend(self.graph[c_n])

    def is_cyclic_util(self, current_n, visited, parent):
        visited.add(current_n)

        return any(
            n not in visited
            and self.is_cyclic_util(n, visited, current_n)
            or n in visited
            and n != parent
            for n in self.graph[current_n]
        )

    def is_cycle(self):
        visited = set()

        for n in self.graph:
            if n not in visited:
                if self.is_cyclic_util(n, visited, None):
                    return True
        return False


g = Graph()

for i in range(1, 5):
    g.add_node(i)

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
print("Graph Contents : ")
g.BFS(1)

print()
g.DFS(1)
print()

print('Is the graph cyclic? - >', g.is_cycle())
