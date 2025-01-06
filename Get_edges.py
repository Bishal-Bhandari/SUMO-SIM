from sumolib import checkBinary, net

# Load network
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# Start and end edges
start_edge = "-109507282"
end_edge = "-109829810#0"

# Find connected route
try:
    route_edges, _ = network.getShortestPath(network.getEdge(start_edge), network.getEdge(end_edge))
    edge_ids = [edge.getID() for edge in route_edges]
    print("Complete Route:", " -> ".join(edge_ids))
except Exception as e:
    print(f"Error finding route: {e}")
    exit()


