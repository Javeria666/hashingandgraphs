from helper_functions import *
G = {'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
print("GRAPH")
print(G)
print()

max_inbound = max_outbound = 0
airport_max_inbound = None
airport_max_outbound = None
for airport, neighbors in G.items():
    inbound = len(getInNeighbors(G, airport))
    outbound = len(getOutNeighbors(G,airport))
    if inbound > max_inbound:
        max_inbound = inbound
        airport_max_inbound = airport
    if outbound > max_outbound:
        max_outbound = outbound
        airport_max_outbound = airport

print("MAXIMUM IN-BOUND:", airport_max_inbound)
print("MAXIMUM OUT BOUND:", airport_max_outbound)


'''
EXPECTED OUTPUT:

GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}

MAXIMUM IN-BOUND: Atlanta
MAXIMUM OUT-BOUND: Dallas
'''