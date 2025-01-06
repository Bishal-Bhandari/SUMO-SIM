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


# Function to get the ordered list of edges
def sort_edges_serially(edge_list, net):
    sorted_edges = []
    visited = set()

    # Start with the first edge
    current_edge_id = edge_list[0]
    sorted_edges.append(current_edge_id)
    visited.add(current_edge_id)

    while len(sorted_edges) < len(edge_list):
        current_edge = net.getEdge(current_edge_id)
        next_edge = None

        # Find the next edge connected to the current edge
        for out_edge in current_edge.getOutgoing():
            out_edge_id = out_edge.getID()
            if out_edge_id in edge_list and out_edge_id not in visited:
                next_edge = out_edge_id
                break

        if next_edge:
            sorted_edges.append(next_edge)
            visited.add(next_edge)
            current_edge_id = next_edge
        else:
            print(f"Warning: Could not find a connection for edge {current_edge_id}")
            break

    return sorted_edges


# Sort the edges
sorted_edges = sort_edges_serially(edges_from_file, network)

# Print the sorted edges
print("Sorted Edges:", " -> ".join(sorted_edges))