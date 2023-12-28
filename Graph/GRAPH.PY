class Graph:
  def __init__(self, directed = False):
    self.graph = {}
    self.directed = directed 

# -------------------------------------------------------------------------------------------------------

  def Add_Node(self,node):
    self.graph[node] = []
# -------------------------------------------------------------------------------------------------------

  def Add_edge(self, v1, v2):
      if v1 not in self.graph or v2 not in self.graph:
         print('Entered Node is not in the graph')
      else:
          self.graph[v1].append(v2)
          if not self.directed:
             self.graph[v2].append(v1)
# -------------------------------------------------------------------------------------------------------

  def delete_Node(self, Node):
    del self.graph[Node]
    for n in self.graph:
      self.graph[n] = [i for i in  self.graph[n] if i!=Node]
# -------------------------------------------------------------------------------------------------------

  def delete_edge(self , node1 , node2):
    self.graph[node1] = [ i for i in self.graph[node1] if i != node2]
    if not self.directed :
      self.graph[node2] = [ i for i in self.graph[node2] if i != node1]

# -------------------------------------------------------------------------------------------------------

  def DFS(self , start_node):
    visited = set()
    stack = [start_node]

    while stack:
      node = stack.pop()
      if node not in visited:
        visited.add(node)
        print(node , end='')

        stack.extend(i for i in self.graph[node] if i not in visited)
# -------------------------------------------------------------------------------------------------------

  def Bfs(self, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
      node = queue.pop(0)
      print(node , end= ' ')

      for i in self.graph[node]:
        if i not in visited :
          visited.add(i)
          queue.append(i)
          
# -------------------------------------------------------------------------------------------------------          
Ungraph = Graph()
Ungraph.Add_Node("Z")
Ungraph.Add_Node("A")
Ungraph.Add_Node("H")
Ungraph.Add_Node("E")
Ungraph.Add_Node("E")
Ungraph.Add_Node("R")

Ungraph.Add_edge('Z' , 'R')
Ungraph.Add_edge('A' , 'Z')
Ungraph.Add_edge('H' , 'A')
Ungraph.Add_edge('R' , 'A')
Ungraph.Add_edge('E' , 'Z')

# print(Ungraph.graph)
print()
print("DFS traversal:")
Ungraph.DFS("Z")
print()
print("BFS traversal:")
Ungraph.Bfs('Z')
print("After Deleting Node:")
Ungraph.delete_Node("R")
print(Ungraph.graph)
print()
print("After Deleting edge :")
Ungraph.delete_edge('E' , 'Z')
print(Ungraph.graph)


