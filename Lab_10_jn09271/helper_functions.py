def addNodes(G, nodes):
    for i in nodes:
        if i not in G:
            G[i]= []

def addEdges(G, edges, directed=False):
     for edge in edges:
        if directed:
            G[edge[0]].append((edge[1], edge[2]))
        else:
            G[edge[0]].append((edge[1], edge[2]))
            G[edge[1]].append((edge[0], edge[2]))
    

def displayGraph(G):
    print (G)

def listOfNodes(G):
    return list(G.keys())

def listOfEdges(G, directed=False):
    edges = []
    for node in G:
        for neighbor in G[node]:
            if directed:
                edges.append((node, neighbor[0], neighbor[1]))
            else:
                if (neighbor[0], node, neighbor[1]) not in edges:
                    edges.append((node, neighbor[0], neighbor[1]))
    return edges


    

def getNeighbors(G, nodes):
    neighbors = []
    for edge in G[nodes]:
        neighbors.append(edge[0])

    return neighbors

def removeNode(G, node):
    if node in G:
        del G[node]
    for x in G:
        for neighbor in G[x]:
            if neighbor[0] == node:
                G[x].remove(neighbor)


def removeNodes(G, nodes):
    for node in nodes:
        removeNode(G, node)

def getNearestNeighbor(G, node):
      
    near = None
    for neighbor in G[node]:
        if near == None:
            near = neighbor
        elif neighbor[1] < near[1]:
            near = neighbor

    return near[0]