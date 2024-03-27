from helper_functions import *
def main():
    # print("GRAPH")
    # g={'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
    # nodes = listOfNodes(g)
    # edges = listOfEdges(g)
    # adj={}
    # addNodes(adj,nodes)
    # addEdges(adj,edges,True)
    # displayGraph(adj)

    adj = {}
    nodes = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']
    edges = [('Dallas', 'Austin', 200), ('Austin', 'Dallas', 200), ('Washington', 'Dallas', 1300), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Denver', 'Chicago', 1000), ('Chicago', 'Denver', 1000), ('Denver', 'Atlanta', 1400), ('Austin', 'Houston', 160), ('Houston', 'Atlanta', 800), ('Atlanta', 'Houston', 800), ('Atlanta', 'Washington', 600), ('Washington', 'Atlanta', 600)]
    
    # nodes = listOfNodes(adj)
    # edges = listOfEdges(adj)
    addNodes(adj, nodes)    
    addEdges(adj, edges, True)  
    
    print("GRAPH")
    print(adj)

    print()
    print("ONE WAY CONNECTION")
    print(one_way_connection(adj))

    print()
    print("NEAREST AIRPORT")
    for node in adj:
        print(node, ":", nearest_airport(adj, node))

    print()
    print("CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT")
    print('Dallas :',not_more_than_one_intermediate(adj, 'Dallas'))

    print()
    removeNode(adj,"Washington")
    addEdges(adj,[('Atlanta','Dallas',1700)],False)
    print("REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH")


    displayGraph(adj)


def one_way_connection(G):
    oneway=[]
    for node in G:
        neighbours=getNeighbors(G,node)
        for neighbour in neighbours:
            if node not in getNeighbors(G,neighbour):
                oneway.append((node,neighbour))
    return oneway

def nearest_airport(G, A):
    return getNearestNeighbor(G,A)

def not_more_than_one_intermediate(G, node):
    connected_w_node=[]
    output=[]
    for i in G: #directly connnected
        if node in getNeighbors(G,i):
            connected_w_node.append(i)
            output.append(i)
    
    for j in connected_w_node: #one intermediate
        for i in G:
            if j in getNeighbors(G,i) and i not in output and i!=node:
                output.append(i)
    return output
if __name__=="__main__":
    main()


'''
EXPECTED OUTPUT:

GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}

ONE WAY CONNECTION
[('Dallas', 'Denver'), ('Dallas', 'Chicago'), ('Austin', 'Houston'), ('Washington', 'Dallas'), ('Denver', 'Atlanta')]

NEAREST AIRPORT
Dallas : Austin
Austin : Houston
Washington : Atlanta
Denver : Chicago
Atlanta : Washington
Chicago : Denver
Houston : Atlanta

CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT
Dallas : ['Austin', 'Washington', 'Atlanta']

REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900), ('Atlanta', 1700)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Houston', 800), ('Dallas', 1700)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
'''