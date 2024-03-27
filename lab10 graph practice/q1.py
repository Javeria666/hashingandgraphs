from helper_functions import *
print("GRAPH")
G={1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}
displayGraph(G)
print()

print("LIST OF NODES")
nodes= listOfNodes(G)
print(nodes)
print()


print("LIST OF EDGES")
print(listOfEdges(G))
print()

print("NEIGHBOURS FOR EACH NODE IN A GRAPH")
for n in G:
    print(n,":", getNeighbors(G,n))
'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}

LIST OF NODES
[1, 2, 3, 4, 5]

LIST OF EDGES
[(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]

NEIGHBOURS FOR EACH NODE IN A GRAPH
1 : [2, 5]
2 : [1, 3, 4, 5]
3 : [2, 4]
4 : [2, 3, 5]
5 : [1, 2, 4]
'''