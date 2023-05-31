graph = {}

def add_node(v):
    if v in graph:
        print(v , 'is already present in the graph')
    else:
        graph[v] = []
        
        
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1 , 'is Not present in the graph')
    elif v2 not in graph:
        print(v2 , 'is not present in the graph')
        
    else:
        #undirected  graph
        graph[v1].append(v2)
        graph[v2].append(v1)
        
        
        #directed Graph
        # graph[v1].append(v2)

        
def  delete_node(v):
    if v not in graph:
        print(v , 'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)
                
def delete_edge(v1,v2):
    if v1 in graph and v2 in graph[v1]:
        graph[v1].remove(v2)
        
def print_graph():
        for node in graph:
            print(node, "->", " -> ".join(str(i) for i in graph[node]))


add_node(1)
add_node(2)
add_node(3)
add_node(4)


add_edge(1, 2)
add_edge(1, 3)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 1)
add_edge(1, 2)
add_edge(1, 3)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 1)
add_edge(1, 2)
add_edge(1, 3)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 1)
add_edge(1, 2)
add_edge(1, 3)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 1)

print("Before deletion:")
print_graph()

node_to_delete = 2
delete_node(node_to_delete)

edge_to_delete_src = 1
edge_to_delete_dest = 3
delete_edge(edge_to_delete_src, edge_to_delete_dest)

print("\nAfter deletion of edge ({}, {}):".format(edge_to_delete_src, edge_to_delete_dest))
print_graph()