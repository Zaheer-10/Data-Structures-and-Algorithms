class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def delete_node(self, node):
        del self.graph[node]
        for n in self.graph:
            self.graph[n] = [x for x in self.graph[n] if x != node]

    def delete_edge(self, node1, node2):
        self.graph[node1] = [x for x in self.graph[node1] if x != node2]
        if not self.directed:
            self.graph[node2] = [x for x in self.graph[node2] if x != node1]

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        visited.add(start_node)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def display_graph(self):
        for node, neighbors in self.graph.items():
            print(f"Node {node}: {neighbors}")


# Example usage:

# Create an undirected graph
undirected_graph = Graph()

# Add nodes
undirected_graph.add_node('A')
undirected_graph.add_node('B')
undirected_graph.add_node('C')
undirected_graph.add_node('D')
undirected_graph.add_node('E')
undirected_graph.add_node('F')
undirected_graph.add_node('G')


# Add edges
undirected_graph.add_edge('A' , 'B')
undirected_graph.add_edge('B' , 'E')
undirected_graph.add_edge('A', 'C')
undirected_graph.add_edge('B','D')
undirected_graph.add_edge('F','C')
undirected_graph.add_edge('F','G')
undirected_graph.add_edge('G','D')


# Display all key-value pairs in the undirected graph
undirected_graph.display_graph()

# Perform DFS traversal starting from node 1
print("DFS traversal:")
undirected_graph.dfs('A')
print()

# Perform BFS traversal starting from node 1
print("BFS traversal:")
undirected_graph.bfs('A')
print()

undirected_graph.delete_edge("F" , "C")

# Delete a node and corresponding edges
# undirected_graph.delete_node(2)
print("After deleting")
# Display all key-value pairs in the undirected graph after deleting node 2
undirected_graph.display_graph()

# Perform DFS traversal after deleting node 2
# print("DFS traversal after deleting node 2:")
# undirected_graph.dfs(1)
# print()

# Perform BFS traversal after deleting node 2
# print("BFS traversal after deleting node 2:")
# undirected_graph.bfs(1)
# print()

# Create a directed graph
# directed_graph = Graph(directed=True)

# Add nodes
# directed_graph.add_node('A')
# directed_graph.add_node('B')
# directed_graph.add_node('C')
# directed_graph.add_node('D')
# directed_graph.add_node('E')
# directed_graph.add_node('F')


# Add edges
# directed_graph.add_edge(1, 2)
# directed_graph.add_edge(2, 3)
# directed_graph.add_edge(3, 4)
# directed_graph.add_edge(4, 1)

# Display all key-value pairs in the directed graph
# directed_graph.display_graph()

# Perform DFS traversal starting from node 1
# print("DFS traversal:")
# directed_graph.dfs(1)
# print()

# Perform BFS traversal starting from node 1
# print("BFS traversal:")
# directed_graph.bfs(1)
# print()

# Delete an edge
# directed_graph.delete_edge(1, 2)

# Display all key-value pairs in the directed graph after deleting the edge
# directed_graph.display_graph()

# Perform DFS traversal after deleting the edge
# print("DFS traversal after deleting the edge:")
# directed_graph.dfs(1)
# print()

# Perform BFS traversal after deleting the edge
# print("BFS traversal after deleting the edge:")
# directed_graph.bfs(1)
# print()
