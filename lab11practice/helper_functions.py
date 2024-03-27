import csv

##############################################################################################
############################# COPY YOUR LAB10 FUNCTIONS HERE #################################

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

##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################

def in_out_degree(G):
    inout={}
    for n in G:
        inout[n]=(len(getInNeighbors(G,n)),len(getOutNeighbors(G,n)))
    return inout
   
    

def degree(G):
    degree={}
    for n in G:
        degree[n]= len(G[n])
    return degree
    

def getInNeighbors(G, node):
    inn=[]
    l = listOfEdges(G,True)
    for edge in l:
        if edge[1]==node:
            inn.append(edge[0])
    return inn


def getOutNeighbors(G, node):
    out=[]
    for i in G[node]:
        out.append(i[0])
    return out

def isNeighbor(G, node1, node2):
    for n in G[node1]:
        if n[0]==node2:
            return True
    return False

##############################################################################

def initialize_matrix(rows, cols):
    return [[-1 for _ in range(cols)]for _ in range (rows)]



def adjlst_to_adj_matrix(G):
    nodes = listOfNodes(G)
    n=len(G)
    adj_matrix= initialize_matrix(n,n)
    row=0
    for node in G:
        for edge in G[node]:
            idx = nodes.index(edge[0])
            adj_matrix[row][idx] = edge[1]
        row+=1

    return adj_matrix


##############################################################################

def csv_to_adj_list(filename):
    adjacency_list = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the first row (header)
        for i, row in enumerate(reader):
            node = header[i + 1]  # Skip the first column (node names)
            neighbors = [(header[j + 1], int(val)) for j, val in enumerate(row[1:]) if val != '-1' and val != '0']
            adjacency_list[node] = neighbors
    return adjacency_list
