from sumolib import checkBinary, net

# Load network
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# Start and end edges
start_edge = "38033459"
end_edge = "-199523015"

# Find connected route
route_edges = network.getShortestPath(network.getEdge(start_edge), network.getEdge(end_edge))

# Extract edge IDs
edge_ids = [edge.getID() for edge in route_edges[0]]

# Print full route
print("Complete Route:", " -> ".join(edge_ids))
