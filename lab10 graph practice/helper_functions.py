def addNodes(G, nodes):
    for node in nodes:
        G[node] = []

def addEdges(G, edges, directed=False):
    if directed == False:
        for trip in edges: #edges = [(node1,node2,weight),...]
            G[trip[0]].append((trip[1],trip[2]))
            G[trip[1]].append((trip[0],trip[2]))
    else:
        for trip in edges: #edges = [(node1,node2,weight),...]
            G[trip[0]].append((trip[1],trip[2]))

            


def displayGraph(G):
    print(G)

def listOfNodes(G):
    nodes=[]
    for k in G:
        nodes.append(k)
    return nodes

def listOfEdges(G, directed=False):
    edges=[]    
    for node in G:
        for tup in G[node]:
            if directed:
                edges.append((node,tup[0],tup[1]))
            else:
                if (tup[0],node,tup[1]) not in edges:
                    if (node,tup[0],tup[1]) not in edges:                   
                        edges.append((node,tup[0],tup[1]))
    return edges



def getNeighbors(G, nodes):
    neighbours=[]
    for tup in G[nodes]:
        neighbours.append(tup[0])
    return neighbours

def removeNode(G, node):
    if node in G:
        del G[node]

    for any_node in G:
        for tup in G[any_node]:
            if tup[0]==node:
                G[any_node].remove(tup)


def removeNodes(G, nodes):
    for node in nodes:
        removeNode(G,node)

def getNearestNeighbor(G, node):
    near = None
    for tup in G[node]:
        if near == None:
            near = tup
        if tup[1]<near[1]:
            near = tup
    return near[0]
    