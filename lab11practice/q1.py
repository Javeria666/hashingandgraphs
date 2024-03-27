from helper_functions import *
graph = {1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}

print("GRAPH")
print(graph)
print()

print("IN NEIGHBOURS")
for node in graph:
    print(node, ":", getInNeighbors(graph,node))
print()

print("OUT NEIGHBOURS")
for node in graph:
    print(node, ":", getOutNeighbors(graph,node))
print()

print("ADJACENCY MATRIX")
print(adjlst_to_adj_matrix(graph))
print()

sumin=0
sumout=0
sumedge=0
for node in graph:
    in_n= getInNeighbors(graph,node)
    for i in in_n:
        sumin+=1
    out_n=getOutNeighbors(graph,node)
    for j in out_n:
        sumout+=1
edges = listOfEdges(graph)
sumedge = len(edges)

if sumin==sumout==sumedge:
    ans = True
else:
    ans= False
    
print("Sum of the in-degrees of all nodes, the sum of the out-degrees of all nodes and the total number of edges are all equal:",ans)

'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}

IN NEIGHBORS
1 : [3]
2 : [1, 3]
3 : [4]
4 : [2, 4]

OUT NEIGHBORS
1 : [2]
2 : [4]
3 : [1, 2]
4 : [3, 4]

ADJACENCY MATRIX
[[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]

Sum of the in-degrees of all nodes, the sum of the out-degrees of all nodes and the total number of edges are all equal: True  
'''