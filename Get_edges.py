from sumolib import checkBinary, net

# Load network
net_file = "bamberg.net.xml"
network = net.readNet(net_file)

# Load edges from the file
with open("Gaustadt.txt", "r") as file:
    edges = [line.strip().replace("edge:", "") for line in file]

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

# Save the sorted edges to a .rou.xml file
with open("sorted_gaustadt.rou.xml", "w") as f:
    f.write('<routes>\n')
    f.write('<vType id="bus" vClass="bus" accel="1.0" decel="4.0" length="12" maxSpeed="20" color="1,0,0"/>\n')
    f.write(f'<route id="route1" edges="{" ".join(sorted_edges)}"/>\n')
    f.write('<vehicle id="bus_1" type="bus" route="route1" depart="0"/>\n')
    f.write('</routes>\n')

print("Sorted route saved to sorted_gaustadt.rou.xml")