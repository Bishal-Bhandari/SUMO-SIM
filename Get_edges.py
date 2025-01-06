from sumolib import net

# Load the SUMO network file
net_file = "bamberg.net.xml"  # Replace with your actual .net.xml file
network = net.readNet(net_file)

# Load edges from the file
with open("Gaustadt.txt", "r") as file:
    edges = [line.strip().replace("edge:", "") for line in file]

# Function to sort edges serially
def sort_edges_serially(edge_list, net):
    sorted_edges = []
    visited = set()

    # Start with the first edge in the list
    current_edge_id = edge_list[0]
    sorted_edges.append(current_edge_id)
    visited.add(current_edge_id)

    while len(sorted_edges) < len(edge_list):
        current_edge = net.getEdge(current_edge_id)
        next_edge = None

        # Find the next connected edge
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
            print(f"Warning: No connection found for edge {current_edge_id}")
            break

    return sorted_edges

# Sort the edges
sorted_edges = sort_edges_serially(edges, network)

# Save sorted edges to a file
with open("sorted_edges.txt", "w") as file:
    for edge in sorted_edges:
        file.write(f"edge:{edge}\n")

print("Sorted edges saved to sorted_edges.txt")
