class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def delete_node(self, node):
        del self.graph[node]
        for n in self.graph:
            self.graph[n] = [x for x in self.graph[n] if x != node]

    def delete_edge(self, node1, node2):
        self.graph[node1] = [x for x in self.graph[node1] if x != node2]
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

# Create a new graph
graph = Graph()

# Add nodes
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

# Add edges
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

# Display all key-value pairs in the graph
graph.display_graph()

# Perform DFS traversal starting from node 1
print("DFS traversal:")
graph.dfs(1)
print()

# Perform BFS traversal starting from node 1
print("BFS traversal:")
graph.bfs(1)
print()

# Delete a node and corresponding edges
graph.delete_node(2)

# Display all key-value pairs in the graph after deleting node 2
graph.display_graph()

# Perform DFS traversal after deleting node 2
print("DFS traversal after deleting node 2:")
graph.dfs(1)
print()

# Perform BFS traversal after deleting node 2
print("BFS traversal after deleting node 2:")
graph.bfs(1)
print()