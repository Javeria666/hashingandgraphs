from helper_functions import *
def main():
    graph = {}
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]

    addNodes(graph, nodes)
    addEdges(graph, edges, False)

    nodes = listOfNodes(graph)
    edges = listOfEdges(graph)

    print("GRAPH")
    print(graph)
    print()


    print("LIST OF NODES")
    print(nodes)
    print()

    
    print("LIST OF EDGES")
    print(edges)
    print()

    print("NEIGHBOURS FOR EACH NODE IN A GRAPH")
    for node in graph:
        print(node, ":", getNeighbors(graph, node))

if __name__ == "__main__":
    main()

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