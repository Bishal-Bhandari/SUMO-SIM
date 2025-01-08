from sumolib import net

# Load the network file
net_file = "NET.net.xml"  # Replace with your .net.xml file path
network = net.readNet(net_file)

# Edges to check
from_edge = "192960749"
to_edge = "121065090"

# Check connectivity
try:
    path = network.getShortestPath(network.getEdge(from_edge), network.getEdge(to_edge))
    if path:
        print(f"Valid path found: {[edge.getID() for edge in path[0]]}")
    else:
        print(f"No path found between {from_edge} and {to_edge}")
except Exception as e:
    print(f"Error: {e}")
