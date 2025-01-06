from sumolib import checkBinary, net

# Load network
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# Input list of edges
edges_from_file = [
    "-109507282", "-109829810#0", "-1130839432", "-1135618619", "-1135618621",
    "-117367372#1", "-117367373#2", "-118319060#0", "-118321787#4",
    # Add all edges from your file here
]

# Find connected route
try:
    route_edges, _ = network.getShortestPath(network.getEdge(start_edge), network.getEdge(end_edge))
    edge_ids = [edge.getID() for edge in route_edges]
    print("Complete Route:", " -> ".join(edge_ids))
except Exception as e:
    print(f"Error finding route: {e}")
    exit()


