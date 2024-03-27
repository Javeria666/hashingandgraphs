from helper_functions import *

def main():
    graph = {}
    nodes = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']
    edges = [('Dallas', 'Austin', 200), ('Austin', 'Dallas', 200), ('Washington', 'Dallas', 1300), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Denver', 'Chicago', 1000), ('Chicago', 'Denver', 1000), ('Denver', 'Atlanta', 1400), ('Austin', 'Houston', 160), ('Houston', 'Atlanta', 800), ('Atlanta', 'Houston', 800), ('Atlanta', 'Washington', 600), ('Washington', 'Atlanta', 600)]

    addNodes(graph, nodes)    
    addEdges(graph, edges, True)
    nodes = listOfNodes(graph)
    edges = listOfEdges(graph)
    print("GRAPH")
    print(graph)

    print()
    print("ONE WAY CONNECTION")
    print(one_way_connection(graph))

    print()
    print("NEAREST AIRPORT")
    for node in graph:
        print(node, ":", nearest_airport(graph, node))

    
    print()
    print("CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT")
    print('Dallas :',not_more_than_one_intermediate(graph, 'Dallas'))
    
    print()
    removeNode(graph, 'Washington')
    addEdges(graph, [('Atlanta', 'Dallas', 1700)], False)
    print("REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH")
    displayGraph(graph)

def one_way_connection(G):

    one_way = []

    for node in G:
        neighbors = getNeighbors(G, node)
        for neighbor in neighbors:
            if node not in getNeighbors(G, neighbor):
                one_way.append((node, neighbor))
    
    return one_way

def nearest_airport(G, A):    
    return getNearestNeighbor(G, A)

def not_more_than_one_intermediate(G, node):
    connected = []
    result = []

    for n in G:
        if node in getNeighbors(G, n):
            connected.append(n)
            result.append(n)

    for i in connected:
        for n in G:
            if i in getNeighbors(G, n) and n not in result and n != node:
                result.append(n)

    return result

if __name__ == "__main__":
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